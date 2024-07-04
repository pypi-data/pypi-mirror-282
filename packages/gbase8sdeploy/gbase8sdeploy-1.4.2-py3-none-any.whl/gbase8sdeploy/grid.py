# coding: utf8


class Grid:
    auto_id = 0

    def __init__(self, er_domain, name, *args):
        """
        :param er_domain: ERDomin，所属的ER域
        :param name: str, 网格的名称
        :param args: [ERNode],定义网格中的节点，不指定时默认all
        """
        self._er_domain = er_domain
        if not name:
            self._name = 'grid_' + str(Grid.get_auto_id())
        else:
            self._name = name
        self._grid_specific_nodes = args if len(args) > 0 else None

    @property
    def name(self) -> str:
        """
        网格名称
        :return: str
        """
        return self._name

    @staticmethod
    def get_auto_id():
        Grid.auto_id += 1
        return Grid.auto_id

    def define(self):
        """
        定义网格
        :return: None
        """
        cmd = f"cdr define grid {self.name}"
        if not self._grid_specific_nodes:
            cmd += " --all"
        else:
            for node in self._grid_specific_nodes:
                cmd += f" {node.group_name}"
        code, out = self._er_domain.root_node.run_cmd(cmd)
        if code != 0:
            raise Exception(f"执行{cmd}失败，错误码：{code}, 错误信息：{out}")

    def enable(self, node=None, user: str = None):
        """
        指定网格上的哪个节点使用什么用户可以连接网格
        :param node: ERNode
        :param user: str
        :return: None
        """
        if not node and not user:
            raise Exception('至少需要设置参数node和user中的一个')
        cmd = f"cdr enable grid --grid={self.name}"
        if node:
            cmd += f" --node={node.group_name}"
        if user:
            cmd += f" --user={user}"
        code, out = self._er_domain.root_node.run_cmd(cmd)
        if code != 0:
            raise Exception(f"执行{cmd}失败，错误码：{code}, 错误信息：{out}")

    def disable(self, node=None, user: str = None):
        """
        禁用网格上指定节点
        :param node: ERNode
        :param user: str
        :return: None
        """
        cmd = f"cdr disable grid --grid={self.name}"
        if node:
            cmd += f" --node={node.group_name}"
        if user:
            cmd += f" --user={user}"
        code, out = self._er_domain.root_node.run_cmd(cmd)
        if code:
            raise Exception(f"执行{cmd}失败，错误码： {code}, 错误信息： {out}")
