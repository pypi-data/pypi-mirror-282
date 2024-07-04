# coding: utf-8
# @Time    : 2024/3/6 9:15
# @Author  : wangwei
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gbase8sdeploy.sqlhosts import SqlHosts

'''
定义GBase8s中操作的实体的抽象类， 包括实例和CM
'''


class Instance(metaclass=ABCMeta):
    """
    数据库服务实体（SERVER、CM）抽象类
    """
    def __init__(self):
        self._name = None
        self._ip = None
        self._port = None
        self._onconfig = None
        self._sqlhosts = None
        self._env = None
        self._product = None

    @property
    def name(self):
        """
        返回实体名称
        :return: str
        """
        return self._name

    @property
    def ip(self):
        """
        返回实体ip
        :return: str
        """
        return self._ip

    @property
    def port(self):
        """
        返回实体服务端口
        :return: int
        """
        return self._port

    @property
    def onconfig(self):
        """
        返回实体的onconfig实例
        :return: ONCONFIG
        """
        return self._onconfig

    @property
    def sqlhosts(self) -> SqlHosts:
        """
        返回实体的sqlhosts实例
        :return: SQLHOSTS
        """
        return self._sqlhosts

    @property
    def env(self):
        """
        返回实体的环境实例
        :return: ENV
        """
        return self._env

    @property
    def session(self):
        """
        返回操作实体的SSHSession实例
        :return: SSHSession
        """
        _session = self._product.session
        _session.env = self.env
        return _session

    @abstractmethod
    def startup(self):
        """
        启动实体
        :return:
        """
        pass

    @abstractmethod
    def shutdown(self):
        """
        关停实体
        :return:
        """
        pass

    def run_cmd(self, cmd, **kwargs):
        """
        在实体环境中运行shell命令
        :param cmd: str, 命令字符串
        :param kwargs: 相关参数，参考SSHSession.run_cmd
        :return: 参考SSHSession.run_cmd
        """
        code, out = self.session.run_cmd(cmd, **kwargs)
        return code, out

    def run_cmd_in_channel(self, cmd, **kwargs):
        """
        shell命令
        :param cmd: str, 命令字符串
        :param kwargs: cwd: 工作目录 username: 执行命令的用户 timeout: 超时时间
        :return: stream, exp: for text in stream: print(text, end='')
        """
        return self.session.run_cmd_in_channel(cmd, **kwargs)




