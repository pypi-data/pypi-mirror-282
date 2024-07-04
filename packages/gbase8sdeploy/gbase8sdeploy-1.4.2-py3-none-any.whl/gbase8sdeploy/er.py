# coding: utf-8
# @Author   : wangwei
from typing import Iterator
from gbase8sdeploy.replicate import Replicate
from gbase8sdeploy.replicate_set import ReplicateSet
from gbase8sdeploy.grid import Grid
from gbase8sdeploy.server import Server, SpaceAlreadyExists
from gbase8sdeploy.cluster import Cluster
from gbase8sdeploy.er_node import ServerNode
from gbase8sdeploy.er_node import ClusterNode
from gbase8sdeploy.er_node import ERNode


class ERDomain:
    """
    企业级复制类
    """

    def __init__(self):
        self._root_node = None
        self._replicate_list: list[Replicate] = []

    @property
    def root_node(self) -> ERNode:
        """
        当前复制域的根节点
        :return: ERNode
        """
        return self._root_node

    @root_node.setter
    def root_node(self, er_node: ERNode):
        self._root_node = er_node
        self._root_node.type = ERNode.ERNodeType.ER_ROOT

    def get_root_node(self, instance) -> ERNode:
        """
        以指定实体作为当前复制域的根节点，并返回ERNode
        :param instance: Server|Cluster
        :return: ERNode
        """
        if isinstance(instance, Server):
            self.root_node = ServerNode(instance)
        elif isinstance(instance, Cluster):
            self.root_node = ClusterNode(instance)
        return self.root_node

    def sqlhosts_init(self):
        """
        初始化所有ER节点的sqlhosts文件
        :return: Node
        """
        all_nodes = list(self.get_all_er_nodes())
        for node in all_nodes:  # 所有ER节点的所有实例都配置组
            node.sqlhosts_init()
        for node in all_nodes:  # 给ER根节点添加其他ER节点的组信息
            if node != self.root_node:
                self.root_node.add_node_to_sqlhosts(node)
        for node in all_nodes:  # 把ER根节点的sqlhosts信息复制到其他er节点
            if node != self.root_node:
                node.set_sqlhosts(self.root_node.get_sqlhosts())

    def get_all_er_nodes(self, er_node: ERNode = None) -> Iterator[ERNode]:
        """
        获取全部ER节点
        :param er_node: ERNode, 可获取指定节点下的全部节点
        :return: Iterator[ERNode]
        """
        if not er_node:
            er_node = self.root_node
            yield self.root_node
        for node in er_node.children:
            yield node
            yield from self.get_all_er_nodes(node)

    def get_empty_replicate(self, name: str = None) -> Replicate:
        """
        获取一个空的复制，获取到空复制后，你需要进行如下操作
        1、通过调用set_xxx相关方法设置选项参数
        2、调用define方法定义复制
        3、调用add_participant方法添加参与者
        4、调用startup方法启动复制
        :param name: str, 复制的名称
        :return: Replicate
        """
        replicate = Replicate(self, name)
        self._replicate_list.append(replicate)
        return replicate

    def get_empty_replicate_set(self, name: str = None) -> ReplicateSet:
        """
        获取一个空的复制集
        :param name: str, 复制集名称
        :return:
        """
        return ReplicateSet(self, name)

    def get_replicate(self, dbname: str, table: str, table_owner: str, name: str = None) -> Replicate:
        """
        按照指定参数获取一个配置好的复制
        :param dbname: str, 参与复制的数据库名称
        :param table: str, 参与复制的表名称
        :param table_owner: str, 表的所有者
        :param name: str, 复制的名称
        :return: Replicate
        """
        replicate = self.get_empty_replicate(name)
        replicate.set_conflict(Replicate.ConflictOption.IGNORE)
        replicate.define()
        select_stmt = f"select * from {table_owner}.{table}"
        for node in self.get_all_er_nodes():
            replicate.add_participant(self.root_node, node, dbname, table, table_owner, select_stmt)
        return replicate

    def get_replicate_set(self, name: str = None) -> ReplicateSet:
        """
        """
        replset = self.get_empty_replicate_set(name)
        replset.define()
        for replicate in self._replicate_list:
            replset.add_replicate(replicate)
        return replset

    def get_grid(self, name: str = None, *args: ERNode) -> Grid:
        """
        获取一个网格
        :param name: str, 网格的名称
        :param args: [ERNode], 指定网格中的节点，不指定是默认全部节点
        :return: Grid
        """
        grid = Grid(self, name, *args)
        grid.define()
        return grid

    def initialize(self):
        """
        初始化复制域
        :return: None
        """
        self.sqlhosts_init()
        all_nodes = [node for node in self.get_all_er_nodes()]
        for node in all_nodes:
            node.set_variable('CDR_QDATA_SBSPACE', 'cdr_qdata_sbspace')
            node.initialize()
            try:
                node.add_dbspace('cdr_qdata_sbspace', 102400, type='SBA')
            except SpaceAlreadyExists:
                pass
        for node in all_nodes:
            node.define_server()
