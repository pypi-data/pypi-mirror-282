# coding: utf-8
# @Time    : 2024/3/5 10:01
# @Author  : wangwei
from gbase8sdeploy.server import Server
import concurrent.futures
import threading, re


class Cluster:
    """
    高可用集群类，具备搭建HDR\RSS\SDS 以及两地三中心的能力
    """
    auto_id = 0

    def __init__(self, primary_node: Server, name: str = None):
        """
        :param primary_node: 搭建集群时作为主节点的Server
        :param name: 集群的名称
        """
        self._primary_node: Server = primary_node
        self._hdr_node = None
        self._sds_nodes = list()
        self._rss_nodes = list()
        self._remote_level0_path = '/tmp/tape_L0'
        self._local_level0_path = 'tape_L0'
        self._new_level0 = True
        self._is_start = False
        self._is_initialize = False
        self._config = {  # 配置集群中节点需统一的参数
            'DRINTERVAL': 30,
            'DRTIMEOUT': 30
        }
        self._name = name if name else f"cluster_{Cluster._get_auto_id()}"
        self._group_name = f"g_{self.name}"

    @property
    def is_start(self) -> bool:
        """
        集群是否启动
        :return: True or False
        """
        return self._is_start

    @property
    def is_initialize(self) -> bool:
        """
        集群是否初始化
        :return: True or False
        """
        return self._is_initialize

    @staticmethod
    def _get_auto_id() -> int:
        Cluster.auto_id += 1
        return Cluster.auto_id

    @property
    def name(self) -> str:
        """
        集群的名称
        :return: str
        """
        return self._name

    @property
    def group_name(self) -> str:
        """
        集群组的名称
        :return: str
        """
        return self._group_name

    @property
    def config(self) -> dict:
        """
        集群要修改的配置信息
        :return: dict
        """
        return self._config

    def set_config(self, key, value):
        """
        修改集群的配置
        :param key: onconfig文件中的key
        :param value: 要修改的值
        :return: None
        """
        self._config[key] = value

    @property
    def new_level0(self) -> bool:
        """
        是否重新生成0级备份
        :return: True or False
        """
        return self._new_level0

    @new_level0.setter
    def new_level0(self, value: bool):
        self._new_level0 = value

    @property
    def remote_level0_path(self) -> str:
        """
        0级别备份的存储路径
        :return: str
        """
        return self._remote_level0_path

    @remote_level0_path.setter
    def remote_level0_path(self, path: str):
        self._remote_level0_path = path

    @property
    def local_level0_path(self) -> str:
        """
        0级备份下载到本地的路径
        :return: str
        """
        return self._local_level0_path

    @local_level0_path.setter
    def local_level0_path(self, path: str):
        self._local_level0_path = path

    @property
    def primary_node(self) -> Server:
        """
        主节点实例
        :return: Server
        """
        return self._primary_node

    @property
    def hdr_node(self) -> Server:
        """
        HDR节点实例
        :return: Server
        """
        return self._hdr_node

    @hdr_node.setter
    def hdr_node(self, hdr: Server):
        self.primary_node.ids.machine.trust(hdr.ids.machine)
        self._hdr_node = hdr
        if self._is_start:
            self.sqlhosts_init()
            self._params_common(hdr)
            self.hdr_init()

    @property
    def sds_nodes(self) -> list[Server]:
        """
        SDS节点实例列表
        :return: [Server]
        """
        return self._sds_nodes

    @property
    def rss_nodes(self) -> list[Server]:
        """
        RSS节点实例列表
        :return: [Server]
        """
        return self._rss_nodes

    def add_sds(self, sds: Server):
        """
        向集群中添加SDS节点
        :param sds: Server
        :return: None
        """
        self.primary_node.ids.machine.trust(sds.ids.machine)
        self._sds_nodes.append(sds)
        if self._is_start:
            self.sqlhosts_init()
            self._params_common(sds)
            if len(self.sds_nodes) == 1:
                self.sds_init(self.primary_node, is_primary=True)
                self.primary_node.set_sds_primary()
            self.sds_init(sds, is_primary=False)
            sds.startup()

    def add_rss(self, rss: Server):
        """
        向集群中添加RSS节点
        :param rss: Server
        :return: None
        """
        self.primary_node.ids.machine.trust(rss.ids.machine)
        self._rss_nodes.append(rss)
        if self._is_start:
            self.sqlhosts_init()
            self._params_common(rss)
            if len(self.rss_nodes) == 1:
                self.primary_node.run_cmd("onmode -wf LOG_INDEX_BUILDS=1")
                self.new_level0 = True
            self.rss_init(rss)

    def remove_rss(self, rss: Server):
        """
        从集群中移除RSS节点
        :param rss: Server
        :return: None
        """
        self.primary_node.delete_rss_from_primary(rss.name)

    def get_all_slaves(self) -> list[Server]:
        """
        获取集群中全部的从节点
        :return: [Server]
        """
        slaves = []
        slaves.extend(self.sds_nodes)
        slaves.extend(self.rss_nodes)
        if self.hdr_node:
            slaves.append(self.hdr_node)
        return slaves

    def get_all_servers(self) -> list[Server]:
        """
        获取集群中全部节点
        :return: [Server]
        """
        servers = self.get_all_slaves()
        servers.insert(0, self.primary_node)
        return servers

    def _params_common(self, node: Server):
        """
        在指定节点上修改集群中配置的参数
        :param node: Server
        :return: None
        """
        for key, value in self.config.items():
            node.onconfig.set_variable(key, value)

    def sds_init(self, node: Server, is_primary: bool):
        """
        将指定节点作为SDS集群节点进行初始化
        :param node: Server
        :param is_primary: 是否是SDS集群的主节点
        :return: None
        """
        tmp_path = f'{node.path}_tmp'
        if not is_primary:
            node.onconfig.set_variable('SDS_ENABLE', '1')
        node.onconfig.set_variable('SDS_PAGING', f'{tmp_path}/sdstmp1,{tmp_path}/sdstmp2')
        node.onconfig.set_variable('SDS_TEMPDBS', f'sdstmpdbs1, {tmp_path}/sdstmpdbs1,2,0,16000')
        self._sds_add_tmp(node, tmp_path)
        if not is_primary:
            if node.ip == self.primary_node.ip:
                node.path = self.primary_node.path

    @staticmethod
    def _sds_add_tmp(node: Server, tmp_path: str):
        """
        给指定节点添加SDS_PAGING和SDS_TEMPDBS用到的chunk文件
        :param node: Server
        :param tmp_path: 文件存储路径
        :return: None
        """
        code, out = node.run_cmd(f"mkdir -p {node.path} {tmp_path};chmod 755 {node.path} {tmp_path}")
        if code != 0:
            raise Exception(f"节点{node.name}创建存储目录失败，错误码{code}, 错误信息{out}")
        code, out = node.run_cmd(
            'touch sdstmp1 sdstmp2;chown gbasedbt:gbasedbt sdstmp1 sdstmp2;chmod 660 sdstmp1 sdstmp2',
            cwd=f'{tmp_path}')
        if code != 0:
            raise Exception(f"节点{node.name}创建sdstmp失败，错误码{code}, 错误信息{out}")
        code, out = node.run_cmd('touch sdstmpdbs1;chown gbasedbt:gbasedbt sdstmpdbs1; chmod 660 sdstmpdbs1',
                                 cwd=f'{tmp_path}')
        if code != 0:
            raise Exception(f"节点{node.name}创建sdstmpdbs失败，错误码{code}, 错误信息{out}")

    def onconfig_init(self):
        """
        依据当前集群的自定义配置修改集群所有节点的onconfig文件
        :return: None
        """
        nodes = self.get_all_servers()
        for node in nodes:
            self._params_common(node)

    def sqlhosts_init(self):
        """
        生成集群所有节点的sqlhosts对象(不写文件)
        :return: None
        """
        group_entry = self.primary_node.sqlhosts.get_group_entry(self.group_name)
        group_entry.add_server(self.primary_node)
        for node in self.get_all_slaves():
            group_entry.add_server(node)
        self.primary_node.sqlhosts.server_entries.clear()
        for node in self.get_all_slaves():
            new_sqlhosts = self.primary_node.sqlhosts.copy()
            new_sqlhosts.path = node.sqlhosts.path
            new_sqlhosts.machine = node.sqlhosts.machine
            node.sqlhosts = new_sqlhosts

    def backup_restore(self, node_backup: Server, node_restore: Server, strage='FILE'):
        """
        执行0级备份和恢复
        :param node_backup: Server，执行0备的节点
        :param node_restore: Server，执行0备恢复的节点
        :param strage: 恢复策略（预留接口，目前仅支持FILE）
        :return: None
        """
        if strage == 'FILE':
            self._backup_restore_with_file(node_backup, node_restore)
        else:
            raise Exception(f"not support the strage <{strage}>")

    def _backup_restore_with_file(self, node_backup: Server, node_restore: Server):
        self._get_backup_file(node_backup)
        node_restore.ids.machine.upload(self.local_level0_path, self.remote_level0_path)
        self._restore_with_file(node_restore, self.remote_level0_path)

    def _get_backup_file(self, node: Server):
        """
        在指定节点执行0级备份，并下载到本地<local_level0_path>
        :param node: Server
        :return: None
        """
        if self.new_level0:
            code, out = node.run_cmd(f"ontape -s -L 0 -t STDIO > {self.remote_level0_path}")
            if code != 0:
                raise Exception(f"节点{node.name}执行0级备份失败，错误码{code}, 错误信息{out}")
            node.ids.machine.download(self.remote_level0_path, self.local_level0_path)
            self.new_level0 = False

    @staticmethod
    def _restore_with_file(node: Server, file: str):
        """
        在指定节点上使用指定的0级备份文件进行恢复
        :param node: Server
        :param file: str
        :return: None
        """
        code, out = node.run_cmd(f'cat {file}|ontape -p -t STDIO', cwd=node.path)
        if code != 0:
            raise Exception(f"节点{node.name}执行备份恢复失败，错误码{code}, 错误信息{out}")

    def hdr_init(self):
        """
        初始化HDR集群环境
        :return: None
        """
        self.primary_node.set_hdr_primary(self.hdr_node.name)
        self.hdr_node.add_chunk_file('rootdbs')
        self.hdr_node.onconfig.set_variable('DRLOSTFOUND', '$GBASEDBTDIR/etc/dr.lostfound')
        self.backup_restore(self.primary_node, self.hdr_node)
        self.hdr_node.set_hdr_secondary(self.primary_node.name)

    def rss_init(self, rss: Server):
        """
        将指定节点作为RSS集群节点进行初始化
        :param rss: Server
        :return: None
        """
        self.primary_node.add_rss_to_primary(rss.name)
        rss.add_chunk_file('rootdbs')
        self.backup_restore(self.primary_node, rss)
        rss.set_rss_primary(self.primary_node.name)

    def startup(self, timeout=30, init_sqlhosts=True, sds_heartbeat=False):
        """
        启动集群
        1、若集群没有初始化过，则进行初始化
        2、若集群初始化过，则依次启动主、从节点
        :param timeout: int, 启动后最大等待时间，若集群状态仍不正常，则抛出异常
        :param init_sqlhosts: bool, 是否重构集群节点的sqlhosts
        :param sds_heartbeat: bool, SDS集群是否配置心跳
        :return: None
        """
        self.onconfig_init()
        if not self._is_initialize:
            if init_sqlhosts:
                self.sqlhosts_init()
            self._initialize(sds_heartbeat)
        else:
            self._startup()
        self.wait_cluster_ok(timeout)  # 启动集群检查

    def _initialize(self, sds_heartbeat):
        """
        集群初始化启动
        :param sds_heartbeat: bool, 搭建SDS是否配置心跳
        :return: None
        """
        if len(self.sds_nodes) > 0:
            self.sds_init(self.primary_node, is_primary=True)
            if sds_heartbeat:
                self.primary_node.onconfig.set_variable('SDS_ALTERNATE', 'sds_alt_comm')
            self.primary_node.initialize()
            if sds_heartbeat:
                self.primary_node.add_dbspace('sds_alt_comm', 102400, 'BBA')
                self.primary_node.run_cmd('onmode -l')
            self.primary_node.set_sds_primary()
            for node in self.sds_nodes:
                self.sds_init(node, is_primary=False)
                if sds_heartbeat:
                    node.onconfig.set_variable('SDS_ALTERNATE', 'sds_alt_comm')
                node.startup()
        else:
            self.primary_node.initialize()
        if len(self.rss_nodes) > 0:
            self.primary_node.run_cmd('onmode -wf LOG_INDEX_BUILDS=1')
            for node in self.rss_nodes:
                node.sqlhosts.to_file()
                if sds_heartbeat:
                    node.add_chunk_file('sds_alt_comm_1')
                self.rss_init(node)
        if self.hdr_node:
            self.hdr_node.sqlhosts.to_file()
            if sds_heartbeat:
                self.hdr_node.add_chunk_file('sds_alt_comm_1')
            self.hdr_init()
        self._is_initialize = True
        self._is_start = True

    def _startup(self):
        """
        集群直接启动
        :return: None
        """
        self.primary_node.startup()
        for slave in self.get_all_slaves():
            slave.startup()
        self._is_start = True

    def shutdown(self):
        """
        关闭集群，先关从节点，再关主节点
        :return:
        """
        for slave in self.get_all_slaves():
            slave.shutdown()
        self.primary_node.shutdown()
        self._is_start = False

    def wait_cluster_ok(self, timeout=30):
        """
        等待集群状态正常
        :param timeout: int，超时时间
        :return:
        """
        stop_event = threading.Event()
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self._check_status, stop_event)
            try:
                future.result(timeout=timeout)  # 设定超时时间，单位是秒
            except concurrent.futures.TimeoutError:
                stop_event.set()
                raise Exception("Cluster startup timed out!")

    def _check_status(self, event):
        slave_tup = [i.name for i in self.get_all_slaves()]
        while not event.is_set():
            code1, out1 = self.primary_node.run_cmd("onstat -g cluster")
            status_dic = self.handle_node_info(out1)
            if set(slave_tup) == set(status_dic.keys()) and set(status_dic.values()) == {True}:
                break

    @staticmethod
    def handle_node_info(text):
        """
        将onstat -g cluster获取到的集群信息结构化存储
        :param text: str
        :return: dict
        """
        status_dic = {}  # 存储节点状态
        p_node_info = re.compile(r'\s+\(log, page\)\s+\(log, page\)\s+Updates\s*(.*?)\s+$', re.I | re.DOTALL)
        info_lst = re.findall(p_node_info, text)

        sub_info_lst = info_lst[0].split('\n')
        for info in sub_info_lst:
            nodename = info.split(" ")[0].strip()
            llog_state = info.split(" ")[1].strip()
            constatus = info.split(" ")[-1].strip()
            if "," in constatus:
                constatus = constatus.split(",", 1)[-1]
            else:
                raise Exception("检测到集群信息中最后一列的内容有误！")
            if llog_state != '0,0' and constatus in ['Connected,Active', 'Connected,On']:
                ready = True
            else:
                ready = False
            status_dic[nodename] = ready
        return status_dic

    def add_dbspace(self, name, size, type='BA', offset=0, pagesize=2, chunk_name=None, path='.'):
        """
        给集群添加数据空间（所有节点添加chunk，主节点执行onspaces -c -d）
        :param name: str, 空间名称
        :param size: int, 空间大小（与onspaces命令一致）
        :param type: str, BA|TBA|BBA|SBA|UBA
        :param offset: int, 偏移量
        :param pagesize: int, 页大小
        :param chunk_name: chunk的名称
        :param path: chunk路径
        :return: None
        """
        for slave in self.get_all_slaves():
            slave.add_chunk_file(f"{name}_1", path)
        self.primary_node.add_dbspace(name, size, type=type, offset=offset,
                                      pagesize=pagesize, chunk_name=chunk_name, path=path)
