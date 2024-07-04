# coding: utf8
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from enum import Enum
from gbase8sdeploy.server import Server
from gbase8sdeploy.cluster import Cluster
from typing import Union


class ERNode(metaclass=ABCMeta):
    """
    企业级复制节点类
    """

    class ERNodeType(Enum):
        ER_ROOT = 1
        ER_NONROOT = 2
        ER_LEAF = 3

    def __init__(self, instance):
        """
        :param instance: Server|Cluster, 作为节点的Server或Cluster
        """
        self._instance = instance
        self._group_name = None
        self._type = ERNode.ERNodeType.ER_ROOT
        self._children = []
        self._parent = None
        self._ats = '/tmp'
        self._ris = '/tmp'
        self._idle_timeout = None

    @property
    def instance(self) -> Union[Server, Cluster]:
        """
        节点对应的Server或Cluster
        :return: [Server|Cluster]
        """
        return self._instance

    @property
    def group_name(self) -> str:
        """
        节点的组名
        :return: str
        """
        if not self._group_name:
            if isinstance(self.instance, Server):
                self._group_name = f"g_{self.instance.name}"
            elif isinstance(self.instance, Cluster):
                self._group_name = self.instance.group_name
            else:
                raise Exception('instance type Error')
        return self._group_name

    @property
    def idle_timeout(self) -> int:
        """
        定义节点时的参数：--idle
        :return:
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, timeout: int):
        self._idle_timeout = timeout

    @property
    def ats(self):
        """
        定义节点时的参数：--ats
        :return: str
        """
        return self._ats

    @ats.setter
    def ats(self, path: str):
        self._ats = path

    @property
    def ris(self):
        """
        定义节点时的参数：--ris
        :return: str
        """
        return self._ris

    @ris.setter
    def ris(self, path):
        self._ris = path

    @property
    def parent(self):
        """
        返回当前节点的父节点
        定义节点时的参数：--sync 会采用父节点的group_name
        :return: ERNode
        """
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    @property
    def children(self) -> list[ERNode]:
        """
        返回当前节点的所有子节点
        :return: [ERNode]
        """
        return self._children

    @property
    def type(self) -> ERNode.ERNodeType:
        """
        节点类型
        :return: ERNode.ERNodeType
        """
        return self._type

    @type.setter
    def type(self, node_type: ERNode.ERNodeType):
        self._type = node_type

    def get_child_node(self, instance: Union[Server, Cluster], node_type: ERNodeType):
        """
        以指定Server或Cluster创建ER节点作为当前节点的子节点
        :param instance: [Server, Cluster]
        :param node_type: ERNodeType
        :return: ERNode
        """
        if isinstance(instance, Server):
            er_node = ServerNode(instance)
        elif isinstance(instance, Cluster):
            er_node = ClusterNode(instance)
        else:
            raise Exception('Invalid instance type!')
        er_node.type = node_type
        self._children.append(er_node)
        er_node.parent = self
        return er_node

    @abstractmethod
    def define_server(self):
        pass

    @abstractmethod
    def set_variable(self, key, value):
        pass

    def add_dbspace(self, name, size, type='BA', offset=0, pagesize=2, chunk_name=None, path='.'):
        self.instance.add_dbspace(name, size, type, offset, pagesize, chunk_name, path)

    @abstractmethod
    def sqlhosts_init(self):
        pass

    @abstractmethod
    def add_group(self, group_name, index):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def run_cmd(self, cmd):
        pass

    @abstractmethod
    def add_node_to_sqlhosts(self, node: ERNode):
        pass

    @abstractmethod
    def set_sqlhosts(self, sqlhosts):
        pass

    @abstractmethod
    def get_sqlhosts(self):
        pass


class ServerNode(ERNode):
    """
    使用Server创建的ER节点
    """

    def define_server(self):
        """
        在当前实例上执行cdr define server ..
        :return: None
        """
        self.instance.run_cmd(f'mkdir -p {self.ats} {self.ris}')
        cmd = f'cdr define server --ats={self.ats} --ris={self.ris} --init {self.group_name}'
        if self.parent:
            cmd += f' --sync={self.parent.group_name}'
        if self.idle_timeout:
            cmd += f' --idle={self.idle_timeout}'
        if self.type == ERNode.ERNodeType.ER_NONROOT:
            cmd += ' --nonroot'
        elif self.type == ERNode.ERNodeType.ER_LEAF:
            cmd += ' --leaf'
        code, out = self.instance.run_cmd(cmd)
        if code != 0:
            raise Exception(f'cdr define server失败, 错误码{code}, 错误信息{out}')

    def set_variable(self, key, value):
        """
        设置节点的配置文件参数
        :param key: str
        :param value: [str|int]
        :return: None
        """
        self.instance.onconfig.set_variable(key, value)

    def sqlhosts_init(self):
        """
        初始化ServerNode节点的sqlhosts文件
        :return: None
        """
        group = self.instance.sqlhosts.get_group_entry(name=self.group_name)
        group.add_server(self.instance)
        self.instance.sqlhosts.server_entries.clear()

    def add_group(self, group_name, index):
        """
        节点添加组
        :param group_name: str, 组名
        :param index: int, 组的索引
        :return: None
        """
        # self.instance.sqlhosts.add_group(group_name, index)
        self.instance.sqlhosts.get_group_entry(name=group_name, i=index)

    def add_node_to_group(self, node, group_name):
        """
        将指定节点添加到当前节点sqlhosts文件的指定组中
        :param node: ERNode
        :param group_name: str
        :return:
        """
        group = self.instance.sqlhosts.group_entries.get(group_name)
        if isinstance(node, ServerNode):
            group.add_server(node.instance)
        elif isinstance(node, ClusterNode):
            for server in node.all_servers():
                group.add_server(server)

    def add_node_to_sqlhosts(self, node: ERNode):
        """
        把其他ER节点的sqlhsots合并到当前节点的所有实例的sqlhosts
        :param node: ERNode
        :return:
        """
        if isinstance(node, ServerNode):
            self.instance.sqlhosts.extend(node.instance.sqlhosts)
        elif isinstance(node, ClusterNode):
            self.instance.sqlhosts.extend(node.instance.primary_node.sqlhosts)

    def initialize(self):
        """
        初始化当前ServerNode
        :return: None
        """
        if not self.instance.is_initialize:
            self.instance.initialize()
        else:
            if self.instance.is_start:
                self.instance.shutdown()
            self.instance.startup()

    def run_cmd(self, cmd: str) -> tuple[int, str]:
        """
        在当前节点的实例上执行命令
        :param cmd: str
        :return: [int, str], 状态码和输出信息
        """
        code, out = self.instance.run_cmd(cmd)
        return code, out

    def set_sqlhosts(self, sqlhosts):
        """
        将当前ServerNode的sqlhosts文件内容修改为指定sqlhosts的内容
        :param sqlhosts:
        :return: None
        """
        self.instance.sqlhosts = sqlhosts

    def get_sqlhosts(self):
        """
        返回当前ServerNode的sqlhosts
        :return:
        """
        return self.instance.sqlhosts


class ClusterNode(ERNode):
    """
    使用Cluster创建的ER节点
    """

    def all_servers(self) -> list[Server]:
        """
        获取当前ER节点的所有实例
        :return: [Server]
        """
        return self.instance.get_all_servers()

    def define_server(self):
        """
        定义当前ER节点
        :return:
        """
        for server in self.all_servers():
            server.run_cmd(f'mkdir -p {self.ats} {self.ris}')
        cmd = f'cdr define server --ats={self.ats} --ris={self.ris} --init {self.group_name}'
        if self.parent:
            cmd += f' --sync={self.parent.group_name}'
        if self.idle_timeout:
            cmd += f' --idle={self.idle_timeout}'
        if self.type == ERNode.ERNodeType.ER_NONROOT:
            cmd += ' --nonroot'
        elif self.type == ERNode.ERNodeType.ER_LEAF:
            cmd += ' --leaf'
        code, out = self.instance.primary_node.run_cmd(cmd)
        if code != 0:
            raise Exception(f'cdr define server失败, 错误码{code}, 错误信息{out}')

    def set_variable(self, key, value):
        """
        设置节点的onconfig配置参数
        :param key: str
        :param value: [str|int]
        :return: None
        """
        for server in self.all_servers():
            server.onconfig.set_variable(key, value)

    def sqlhosts_init(self):
        """
        初始化ClusterNode节点的sqlhosts
        :return: None
        """
        self.instance.sqlhosts_init()

    def add_group(self, group_name, index):
        """
        节点添加组
        :param group_name: str, 组名
        :param index: int, 组的索引
        :return: None
        """
        for server in self.all_servers():
            server.sqlhosts.get_group_entry(name=group_name, i=index)

    def add_node_to_sqlhosts(self, node: ERNode):
        """
        把其他ER节点的sqlhsots合并到当前节点的所有实例的sqlhosts
        :param node: ERNode
        :return:
        """
        if isinstance(node, ServerNode):
            for cur_server in self.all_servers():
                cur_server.sqlhosts.extend(node.instance.sqlhosts)
        elif isinstance(node, ClusterNode):
            for cur_server in self.all_servers():
                cur_server.sqlhosts.extend(node.instance.primary_node.sqlhosts)

    def initialize(self):
        """
        初始化当前ClusterNode
        :return: None
        """
        if self.instance.is_start:
            self.instance.shutdown()
        self.instance.startup(init_sqlhosts=False)

    def run_cmd(self, cmd) -> tuple[int, str]:
        """
        在当前节点的主节点上执行命令
        :param cmd: str
        :return: [int, str], 状态码和输出信息
        """
        code, out = self.instance.primary_node.run_cmd(cmd)
        return code, out

    def set_sqlhosts(self, sqlhosts):
        """
        将指定sqlhosts的内容设置到当前ClusterNode中的全部实例
        :param sqlhosts: SqlHosts
        :return:
        """
        for server in self.all_servers():
            server.sqlhosts = sqlhosts

    def get_sqlhosts(self):
        """
        获取当前ClusterNode的sqlhosts
        :return: Sqlhosts
        """
        return self.instance.primary_node.sqlhosts
