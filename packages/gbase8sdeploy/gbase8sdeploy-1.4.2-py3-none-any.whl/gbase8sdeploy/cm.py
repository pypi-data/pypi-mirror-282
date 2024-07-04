# coding: utf-8
# @Time    : 2024/3/5 13:39
# @Author  : wangwei
from gbase8sdeploy.instance import Instance
from gbase8sdeploy.env import ENV
from gbase8sdeploy.sqlhosts import SqlHosts
from gbase8sdeploy.onconfig import CMOnconfig
from gbase8sdeploy.cluster import Cluster
from gbase8sdeploy.server import Server
from gbase8sdeploy.er_node import ServerNode, ClusterNode
from gbase8sdeploy.product import CSDK
from enum import Enum


class CM(Instance):
    """
    GBase 8s CM类
    """

    class UnitType(Enum):
        CLUSTER = 'CLUSTER'
        REPLSET = 'REPLSET'
        GRID = 'GRID'
        SERVERSET = 'SERVERSET'

    def __init__(self, csdk: CSDK, name: str = None):
        """
        :param csdk: CSDK
        :param name: str, CM名称
        """
        super().__init__()
        self._csdk = csdk
        self._product = self.csdk
        self._name = "single_cm" if not name else name
        self._local_ip = self.csdk.machine.ip
        self._log = 1
        self._logfile = '${GBASEDBTDIR}' + '/tmp/{}.log'.format(self.name)
        self._debug = None
        self._cm_timeout = None
        self._event_timeout = None
        self._secondary_event_timeout = None
        self._cm_sqlhosts = 'LOCAL'
        self._sections = []
        self._sqlhosts = SqlHosts(path=f"{self.csdk.path}/etc/sqlhosts.{self.name}", machine=self.csdk.machine)
        self._onconfig = CMOnconfig(self.csdk, self.name)
        self._path = self.csdk.path
        self._env = ENV()
        self._env.set_variable('GBASEDBTDIR', self.csdk.path)
        self._env.set_variable('GBASEDBTSQLHOSTS', self.sqlhosts.path)
        self._env.set_variable('GBASEDBTSERVER', None)
        self._env.set_variable('ONCONFIG', self.onconfig.path)
        self._env.set_variable('PATH', f"{self.csdk.path}/bin:$PATH")
        self._unit_index = 0
        self._cmgroup_info = None
        self._is_start = False
        self._is_initialize = False

    def create_profile(self) -> str:
        """
        创建cm的profile文件
        :return: str, profile文件的绝对路径
        """
        profile_text = str(self.env)
        lines = profile_text.splitlines()
        self.run_cmd(f"echo '# created by pygbase8s' > {self.csdk.path}/profile.{self.name}")
        for line in lines:
            self.run_cmd(f"echo '{line}' >> {self.csdk.path}/profile.{self.name}")
        return f"{self.csdk.path}/profile.{self.name}"

    def create_section(self, serverlist, unit_type: UnitType = UnitType.CLUSTER, unit_name=None):
        """
        创建连接单元
        :param serverlist: Server|Cluster|ERNode|[Server]|[ERNode]
        :param unit_type: CM.UnitType
        :param unit_name: str
        :return: SectionEntry
        """
        self._unit_index += 1
        section = SectionEntry(unit_type.value, unit_name, self)
        section.unit_index = self._unit_index
        self._sections.append(section)
        if isinstance(serverlist, list):
            for _instance in serverlist:
                if isinstance(_instance, Server):
                    # section.servers.append(_instance)
                    section.group_info[section.default_group_name].append(_instance)
                elif isinstance(_instance, ServerNode):
                    section.group_info.update({_instance.group_name: [_instance.instance]})
                elif isinstance(_instance, ClusterNode):
                    section.group_info.update({_instance.group_name: [_s for _s in _instance.all_servers()]})
                else:
                    raise Exception('列表成员类型需要是Server或ERNode')
        elif isinstance(serverlist, Server):
            section.group_info[section.default_group_name].append(serverlist)
        elif isinstance(serverlist, Cluster):
            # servers = serverlist.get_all_slaves()
            # servers.append(serverlist.primary_node)
            # section.group_info[section.default_group_name].extend(servers)
            section.group_info.update({serverlist.group_name: [_s for _s in serverlist.get_all_servers()]})
        elif isinstance(serverlist, ServerNode):
            section.group_info.update({serverlist.group_name: [serverlist.instance]})
        elif isinstance(serverlist, ClusterNode):
            section.group_info.update({serverlist.group_name: [_s for _s in serverlist.all_servers()]})
        else:
            raise Exception('不支持的类型')
        return section

    def reconnect(self):
        """
        重新连接machine
        :return: None
        """
        self.csdk.machine.reconnect()

    @property
    def sections(self):
        """
        当前CM的所有连接单元对象
        :return: [SectionEntry]
        """
        return self._sections

    @property
    def local_ip(self):
        """
        配置参数LOCAL_IP
        :return: str
        """
        return self._local_ip

    @local_ip.setter
    def local_ip(self, ip: str):
        self._local_ip = ip

    @property
    def log(self):
        """
        配置参数LOG
        :return: int
        """
        return self._log

    @log.setter
    def log(self, log: int):
        self._log = log

    @property
    def logfile(self):
        """
        配置参数LOGFILE
        :return: str
        """
        return self._logfile

    @logfile.setter
    def logfile(self, logfile: str):
        self._logfile = logfile

    @property
    def cm_sqlhosts(self):
        """
        配置参数SQLHOSTS
        :return: str
        """
        return self._cm_sqlhosts

    @cm_sqlhosts.setter
    def cm_sqlhosts(self, cm_sqlhosts: str):
        self._cm_sqlhosts = cm_sqlhosts

    @property
    def cm_timeout(self):
        """
        配置参数CM_TIMEOUT
        :return: int
        """
        return self._cm_timeout

    @cm_timeout.setter
    def cm_timeout(self, cm_timeout: int):
        self._cm_timeout = cm_timeout

    @property
    def event_timeout(self):
        """
        配置参数EVENT_TIMEOUT
        :return: int
        """
        return self._event_timeout

    @event_timeout.setter
    def event_timeout(self, event_timeout: int):
        self._event_timeout = event_timeout

    @property
    def secondary_event_timeout(self):
        """
        配置参数SECONDARY_EVENT_TIMEOUT
        :return: int
        """
        return self._secondary_event_timeout

    @secondary_event_timeout.setter
    def secondary_event_timeout(self, secondary_event_timeout: int):
        self._secondary_event_timeout = secondary_event_timeout

    @property
    def debug(self) -> int:
        """
        配置参数DEBUG
        :return: int
        """
        return self._debug

    @debug.setter
    def debug(self, debug: int):
        self._debug = debug

    @property
    def cmgroup_info(self) -> dict:
        """
        CM组信息
        :return: dict
        """
        return self._cmgroup_info

    @cmgroup_info.setter
    def cmgroup_info(self, cmgroup_info):
        self._cmgroup_info = cmgroup_info

    def onconfig_init(self) -> CMOnconfig:
        """
        初始化CM的onconfig文件，并返回onconfig对象
        :return: CMOnconfig
        """
        self._onconfig.initialize()
        if self.local_ip:
            self._onconfig.set_variable('LOCAL_IP', self.local_ip)
        if self.log:
            self._onconfig.set_variable('LOG', self.log)
        if self.logfile:
            self._onconfig.set_variable('LOGFILE', self.logfile)
        if self.cm_sqlhosts:
            self._onconfig.set_variable('SQLHOSTS', self.cm_sqlhosts)
        if self.cm_timeout:
            self._onconfig.set_variable('CM_TIMEOUT', self.cm_timeout)
        if self.event_timeout:
            self._onconfig.set_variable('EVENT_TIMEOUT', self.event_timeout)
        if self.secondary_event_timeout:
            self._onconfig.set_variable('SECONDARY_EVENT_TIMEOUT', self.secondary_event_timeout)
        if self.debug:
            self._onconfig.set_variable('DEBUG', self.debug)

        for section in self.sections:
            self._onconfig.add_cluster_info(str(section))
        return self._onconfig

    def _get_cm_group(self):
        group_info = {}
        for section in self.sections:
            group_info.update(section.group_info)
        return group_info

    def sqlhosts_init(self):
        """
        生成CM的sqlhosts对象(不写文件)
        :return: None
        """
        for group_name, servers in self._get_cm_group().items():
            if len(servers) > 0:
                group = self.sqlhosts.get_group_entry(name=group_name, c=1)
                for server in servers:
                    group.add_server(server)
        if not self.cmgroup_info:  # 如果不配置cm集群
            for section in self.sections:
                self._add_sla_to_cm_group(section.slas)
        else:
            self._add_sla_to_cm_group(self.cmgroup_info)

    def _add_sla_to_cm_group(self, slas: dict):
        """
        依据组和sla的映射关系，添加条目到sqlhsots对象
        :param slas: {group_name: [SLA]}
        :return: None
        """
        for groupname in slas:
            if groupname == "_":    # 不在组里的
                for sla in slas.get(groupname):
                    if not sla.ip:
                        sla.ip = self.csdk.machine.ip
                    if not sla.port:
                        sla.port = self.csdk.machine.get_available_server_port()
                    self.sqlhosts.add_server(sla)
            else:
                group = self.sqlhosts.get_group_entry(name=groupname, c=1)
                for sla in slas.get(groupname):
                    if not sla.ip:
                        sla.ip = self.csdk.machine.ip
                    if not sla.port:
                        sla.port = self.csdk.machine.get_available_server_port()
                    group.add_server(sla)

    @property
    def csdk(self):
        """
        返回CM对应的CSDK实例
        :return: CSDK
        """
        return self._csdk

    @property
    def path(self):
        """
        返回CM的path
        :return: str
        """
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def ip(self):
        """
        返回CM的ip地址
        :return: str
        """
        return self.session.ip

    @property
    def port(self):
        """
        返回cm的监听端口
        :return: int
        """
        return self._port

    def startup(self, reload=False, init_sqlhosts=True):
        """
        启动CM
        :param reload: bool, 启动CM还是重载配置信息
        :param init_sqlhosts: bool, 是否重构CM的sqlhosts
        :return: None
        """
        self.onconfig_init()
        if init_sqlhosts:
            self.sqlhosts_init()
        self.sqlhosts.to_file()
        if reload:
            cmd = f'oncmsm -r {self.name}\n'
        else:
            cmd = f'oncmsm -c {self.onconfig.path}\n'
        code, out = self.run_cmd(cmd, username='gbasedbt')
        if code != 0:
            raise Exception(f"CM启动失败，错误码{code}, 错误信息{out}")
        self._is_initialize = True
        self._is_start = True

    def shutdown(self):
        """
        关停CM
        :return: None
        """
        code, out = self.run_cmd(f'oncmsm -k {self.name}', username='gbasedbt')
        if code != 0:
            raise Exception(f"关停CM失败，错误码{code}, 错误信息{out}")
        self._is_start = False


class SLAEntry:
    """
    SLA类，对应连接单元中的每个SLA
    """

    def __init__(self, name: str, dbservers: str, cm: CM):
        """
        :param name: str， sla的名称
        :param dbservers: str, 连接的节点类型，如ANY|PRI|HDR|SDS ..
        :param cm: CM
        """
        self._name = name
        self._dbservers = dbservers
        self._cm = cm
        self._mode = None
        self._usealiases = None
        self._policy = None
        self._workers = None
        self._ip = self.cm.csdk.machine.ip
        self._port = self.cm.csdk.machine.get_available_server_port()

    @property
    def cm(self) -> CM:
        """
        当前sla所属的cm实例
        :return: CM
        """
        return self._cm

    @cm.setter
    def cm(self, cm: CM):
        self._cm = cm

    @property
    def ip(self) -> str:
        """
        当前sla的ip
        :return: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip: str):
        self._ip = ip

    @property
    def port(self) -> int:
        """
        当前sla的端口
        :return: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        self._port = port

    @property
    def name(self) -> str:
        """
        当前sla的名称
        :return: str
        """
        return self._name

    @property
    def dbservers(self) -> str:
        """
        当前sla配置的DBSERVERS
        :return: str
        """
        return self._dbservers

    @property
    def mode(self) -> str:
        """
        可选参数MODE
        :return: ModeOption
        """
        return self._mode

    @mode.setter
    def mode(self, value: str):
        self._mode = value

    @property
    def usealiases(self) -> str:
        """
        可选参数USEALIASES
        :return: str
        """
        return self._usealiases

    @usealiases.setter
    def usealiases(self, value: bool):
        _value = 'ON' if value else 'OFF'
        self._usealiases = _value

    @property
    def policy(self) -> str:
        """
        可选参数POLICY
        :return: str
        """
        return self._policy

    @policy.setter
    def policy(self, value: str):
        """
        可设置为LATENCY|FAILURE|WORKLOAD|10*LATENCY+FAILURE ..
        :param value: str
        :return: None
        """
        self._policy = value

    @property
    def workers(self) -> int:
        """
        可选参数WORKERS
        :return: int
        """
        return self._workers

    @workers.setter
    def workers(self, value: int):
        self._workers = value

    def __str__(self):
        sla_define = f"SLA {self.name} DBSERVERS={self._dbservers}"
        for param, value in zip(['MODE', 'USEALIASES', 'POLICY', 'WORKERS'],
                                [self.mode, self.usealiases, self.policy, self.workers]):
            if value:
                sla_define += f" {param}={value}"
        return sla_define


class SectionEntry:
    """
    CM的连接单元类
    """

    def __init__(self, unit_type: CM.UnitType, unit_name: str, cm: CM):
        self._unit_type = unit_type
        self._unit_name = unit_name
        self._unit_index = 1
        self._cm = cm
        self._gbasedbtserver = None
        self._cmalarmprogram = None
        self._foc = "FOC ORDER=ENABLED PRIORITY=1 TIMEOUT=0 RETRY=1" if unit_type == 'CLUSTER' else ''
        self._slas: dict[str, list[SLAEntry]] = {}
        self._cmgroup_name = '_'
        self._group_info = None

    @property
    def default_group_name(self) -> str:
        """
        返回默认的server组名
        :return: str
        """
        return f'db_group_{self.unit_index}'

    @property
    def unit_index(self) -> int:
        """
        返回当前连接单元的索引（当前CM中第几个连接单元）
        :return: int
        """
        return self._unit_index

    @unit_index.setter
    def unit_index(self, unit_index):
        self._unit_index = unit_index

    @property
    def group_info(self) -> dict:
        """
        返回当前section的server组信息
        :return: dict
        """
        if not self._group_info:
            self._group_info = {self.default_group_name: []}
        return self._group_info

    @property
    def cm(self) -> CM:
        """
        返回当前section所属的CM
        :return: CM
        """
        return self._cm

    @cm.setter
    def cm(self, cm):
        self._cm = cm

    @property
    def unit_type(self) -> CM.UnitType:
        """
        当前section的类型
        :return: CM.UnitType
        """
        return self._unit_type

    @property
    def unit_name(self) -> str:
        """
        当前section的名称
        :return: str
        """
        if not self._unit_name:
            self._unit_name = f"unit{self.unit_index}"
        return self._unit_name

    @property
    def gbasedbtserver(self) -> str:
        """
        当前section的GBASEDBTSERVER配置
        :return: str
        """
        if not self._gbasedbtserver:
            groups = [group_name for group_name in self.group_info.keys() if len(self.group_info[group_name]) > 0]
            self._gbasedbtserver = ",".join(groups)
        return self._gbasedbtserver

    @gbasedbtserver.setter
    def gbasedbtserver(self, gbasedbtserver):
        self._gbasedbtserver = gbasedbtserver

    @property
    def cmalarmprogram(self) -> str:
        """
        当前section的CMALARMPROGRAM配置
        :return: str
        """
        return self._cmalarmprogram

    @property
    def foc(self) -> str:
        """
        当前section的FOC配置
        :return: str
        """
        return self._foc

    @property
    def slas(self) -> dict[str, list[SLAEntry]]:
        """
        返回当前section中所有的sla对象与组的映射
        :return: dict
        """
        return self._slas

    def create_sla(self, name: str, dbservers: str, cm_group_name=None) -> SLAEntry:
        """
        在section中创建一个sla
        :param name: str, sla的名称
        :param dbservers: str, 例如PRI|SDS|HDR|SDS,HDR
        :param cm_group_name: sla所属组
        :return: SLAEntry
        """
        sla = SLAEntry(name, dbservers, self.cm)
        if not cm_group_name:
            if self._cmgroup_name not in self._slas:
                self._slas[self._cmgroup_name] = [sla]
            else:
                self._slas[self._cmgroup_name].append(sla)
        else:  # 自定义的cm组名
            self._cmgroup_name = cm_group_name
            if cm_group_name not in self._slas:
                self._slas[cm_group_name] = [sla]
            else:
                self._slas[cm_group_name].append(sla)
        return sla

    def set_foc(self, order='ENABLED', priority=1, timeout=0, retry=1):
        """
        设置section的foc
        :param order: str, ENABLED|DISABLED
        :param priority: int
        :param timeout: int
        :param retry: int
        :return: None
        """
        self._foc = f"FOC ORDER={order} PRIORITY={priority} TIMEOUT={timeout} RETRY={retry}"

    def __str__(self):
        if not self.gbasedbtserver:
            raise Exception('serverlist 未设置')
        cmalarm_str = f"CMALARMPROGRAM {self.cmalarmprogram}" if self.cmalarmprogram else ''
        all_slas = []
        for group_slas in self._slas.values():
            all_slas.extend(group_slas)

        slas_str = '\n\t'.join([str(sla) for sla in all_slas])
        text = f"{self.unit_type} {self.unit_name}\n{{\n\tGBASEDBTSERVER {self.gbasedbtserver}\n\t{slas_str}\n\t{self.foc}\n\t{cmalarm_str}\n}}"
        return text


class CMCluster:
    """
    CM集群类，配置CM组，每个组包含多个CM的SLA
    """

    def __init__(self, cm: CM):
        self._cm_pri: CM = cm
        self._slaves: list[CM] = []
        self._merged_dict: dict[str, [SLAEntry]] = {}

    def add_cm(self, cm: CM):
        """
        添加cm对象到集群中
        :param cm: CM
        :return: None
        """
        self._slaves.append(cm)

    def create_section(self, serverlist, unit_type: CM.UnitType = CM.UnitType.CLUSTER, unit_name=None) -> list[
        SectionEntry]:
        """
        给CM集群创建连接单元，返回每个CM节点的section组成的列表
        :param serverlist: Server|Cluster|ERNode|[Server]|[ERNode]
        :param unit_type: CM.UnitType
        :param unit_name: str
        :return: [SectionEntry]
        """
        sections = [self._cm_pri.create_section(serverlist, unit_type, unit_name)]
        for slave in self._slaves:
            sections.append(slave.create_section(serverlist, unit_type, unit_name))
        return sections

    @staticmethod
    def create_sla(sections: list[SectionEntry], name, dbservers, cm_group_name=None) -> [SLAEntry]:
        """
        在输入的sections中创建SLA
        :param sections: [SectionEntry]
        :param name: str, sla的名称
        :param dbservers: str, 例如PRI|SDS|HDR|SDS,HDR
        :param cm_group_name: sla所属组
        :return: [SLAEntry]
        """
        slas = []
        if not cm_group_name:
            cm_group_name = name
        for index, section in enumerate(sections, start=1):
            sla = section.create_sla(name=f"{name}_{index}", dbservers=dbservers, cm_group_name=cm_group_name)
            slas.append(sla)
        return slas

    @staticmethod
    def set_foc(sections: list[SectionEntry], order='ENABLED', timeout=0, retry=1):
        """
        设置输入的sections的FOC，PRIORITY属性递增
        :param sections: [SectionEntry]
        :param order: str
        :param timeout: int
        :param retry: int
        :return: None
        """
        for index, section in enumerate(sections, start=1):
            section.set_foc(order=order, timeout=timeout, retry=retry, priority=index)

    @staticmethod
    def set_sla_options(slas: list[SLAEntry], mode: str = None, policy: str = None, workers: int = None):
        """
        设置输入的sla列表中每个sla的参数
        :param slas: [SLAEntry]
        :param mode: str
        :param policy: str
        :param workers: int
        :return: None
        """
        for sla in slas:
            sla.mode = mode
            sla.policy = policy
            sla.workers = workers

    def get_all_cms(self) -> list[CM]:
        """
        返回cm集群中的全部cm实例
        :return:
        """
        cm_list = [self._cm_pri]
        cm_list.extend(self._slaves)
        return cm_list

    def handle_cm_info(self):
        """
        将cm集群中的所有的sla信息分组合并
        :return: None
        """
        for cm in self.get_all_cms():
            for section in cm.sections:
                for k, v in section.slas.items():
                    if k not in self._merged_dict:
                        self._merged_dict[k] = v.copy()
                    else:
                        self._merged_dict[k].extend(v.copy())

    def startup(self, reload=False):
        """
        启动cm集群
        :param reload: bool
        :return: None
        """
        self.handle_cm_info()
        cm_lst = self.get_all_cms()
        for cm in cm_lst:
            cm.cmgroup_info = self._merged_dict
            cm.startup(reload)

    def shutdown(self):
        """
        关闭cm集群
        :return: None
        """
        self._cm_pri.shutdown()
        for cm in self._slaves:
            cm.shutdown()
