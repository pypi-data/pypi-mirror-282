# coding: utf-8
# @Time    : 2024/4/3 13:32
# @Author  : wangwei
import jaydebeapi
from jaydebeapi import Connection
from abc import ABCMeta, abstractmethod
from gbase8sdeploy.machine import User

'''
按照DB-API接口规范进行封装
'''


class DriverManager(metaclass=ABCMeta):

    def __init__(self, driver_path):
        self._path = driver_path

    @property
    def path(self):
        return self._path

    @abstractmethod
    def connect(self, *args):
        pass


class JDBCDriver(DriverManager):
    """
    JDBC驱动类
    """

    def __init__(self, driver_path):
        """
        :param driver_path: 驱动jar包的路径
        """
        super().__init__(driver_path)
        self._path = driver_path

    def connect(self, server, user: User, dbname: str=None, **kwargs) -> Connection:
        """
        连接指定实例，返回连接对象
        :param server: Server|SLAEntry,要连接的目标实例
        :param user: User
        :param dbname: str, 数据库名称
        :param kwargs: dict， 其他参数，如DB_LOCALE等
        :return: Connection
        """
        variables_str = ';'.join([f'{key}={value}' for key, value in kwargs.items()])
        if variables_str != '':
            variables_str = f':{variables_str}'
        if dbname:
            url = 'jdbc:gbasedbt-sqli://{ip}:{port}' + f'/{dbname}' + f'{variables_str}'
        else:
            url = 'jdbc:gbasedbt-sqli://{ip}:{port}' + f'{variables_str}'
        conn = jaydebeapi.connect(jclassname='com.gbasedbt.jdbc.Driver',
                                  url=url.format(ip=server.ip, port=server.port),
                                  driver_args=(user.username, user.password),
                                  jars=self._path)
        return conn

    def connect_group(self, group_name: str, sqlhostsfile: str, user: User, dbname: str=None, **kwargs) -> Connection:
        """
        连接指定实例组，返回连接对象
        :param group_name: str, sqlhosts文件中的组名
        :param sqlhostsfile: str, sqlhosts文件路径
        :param user: User
        :param dbname: str,数据库名称
        :param kwargs: dict，其他连接参数
        :return: Connection
        """
        params = {
                'GBASEDBTSERVER': group_name,
                'SQLH_FILE': sqlhostsfile,
                'SQLH_TYPE': 'FILE'
            }
        params.update(kwargs)
        variables_str = ':' + ';'.join([f'{key}={value}' for key, value in params.items()])
        if dbname:
            url = 'jdbc:gbasedbt-sqli:' + f'/{dbname}' + f'{variables_str}'
        else:
            url = 'jdbc:gbasedbt-sqli' + f'{variables_str}'
        conn = jaydebeapi.connect(jclassname='com.gbasedbt.jdbc.Driver',
                                  url=url,
                                  driver_args=(user.username, user.password),
                                  jars=self._path)
        return conn


