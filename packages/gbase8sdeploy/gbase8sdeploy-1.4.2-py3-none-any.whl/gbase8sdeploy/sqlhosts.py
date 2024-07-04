# coding: utf8
from __future__ import annotations
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gbase8sdeploy.machine import RemoteMachine
    from gbase8sdeploy.server import Server
    from gbase8sdeploy.cm import SLAEntry


class ServerEntry:

    def __init__(self, servername: str, hostname: str, port: int, connection_type: str = 'onsoctcp', **options):
        self._name = servername
        self._hostname = hostname
        self._servicename = str(port)
        self._connection_type = connection_type
        self._options = options

    @property
    def name(self):
        return self._name

    @property
    def connection_type(self):
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type: str):
        self._connection_type = connection_type

    @property
    def hostname(self):
        return self._hostname

    @property
    def options(self):
        return self._options

    @property
    def servicename(self):
        return self._servicename

    def __str__(self):
        options_str = ",".join([f"{k}={v}" for k, v in self.options.items()])
        return "\t".join([self.name, self.connection_type, self.hostname, str(self.servicename), options_str])


class GroupEntry:

    def __init__(self, name, i, **options):
        self._name: str = name
        self._i: int = i
        self._server_entries: dict[str, ServerEntry] = {}
        self._options = options

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._i

    @number.setter
    def number(self, number: int):
        self._i = number

    @property
    def options(self):
        return self._options

    @property
    def server_entries(self):
        return self._server_entries

    def add_server_item(self, servername, hostname, port, connection_type: str = 'onsoctcp', **options):
        server_entry = ServerEntry(servername, hostname, port, connection_type, **options)
        server_entry.options.update({'g': self.name})
        self.server_entries[server_entry.name] = server_entry

    def add_server_entry(self, server_entry: ServerEntry):
        server_entry.options.update({'g': self.name})
        self._server_entries[server_entry.name] = server_entry

    def add_server(self, server: Union[Server, SLAEntry], connection_type: str = 'onsoctcp', **options):
        """
        添加server到sqlhosts
        :param servername: str, server名称
        :param ip: str, ip
        :param port: int, port
        :return:
        """
        server_entry = ServerEntry(server.name, server.ip, server.port, connection_type, **options)
        server_entry.options.update({'g': self.name})
        self.server_entries[server_entry.name] = server_entry

    def remove_server_entry(self, server_name):
        if server_name in self.server_entries:
            self.server_entries.pop(server_name)

    def copy(self):
        new_group_entry = GroupEntry(self.name, self.number, **self.options)
        new_group_entry.server_entries.update(self.server_entries)
        return new_group_entry

    def __str__(self):
        options = [f"i={self.number}"]
        options.extend([f"{k}={v}" for k, v in self.options.items()])
        options_str = ",".join(options)
        all_lines = ["\t".join([self.name, 'group', '-', '-', options_str])]
        all_lines.extend([str(server_entry) for server_entry in self.server_entries.values()])
        return '\n'.join(all_lines)


class SqlHosts:

    def __init__(self, path: str=None, machine: RemoteMachine=None):
        # self._product = product
        # self._name = name
        self._path = path
        self._machine = machine
        self._server_entries: dict[str, ServerEntry] = {}
        self._group_entries: dict[str, GroupEntry] = {}
        self._group_number = 1


    @property
    def group_number(self):
        return self._group_number

    @group_number.setter
    def group_number(self, number: int):
        self._group_number = number

    @property
    def server_entries(self):
        return self._server_entries

    @property
    def group_entries(self):
        return self._group_entries

    # @property
    # def product(self):
    #     return self._product
    #
    # @product.setter
    # def product(self, product):
    #     self._product = product
    #
    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, name):
    #     self._name = name

    @property
    def path(self):
        """
        返回文件路径
        :return: str
        """
        # return f"{self.product.path}/etc/sqlhosts.{self.name}"
        if not self._path:
            raise Exception('sqlhosts未设置path')
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def machine(self):
        """
        返回所在的机器
        :return: RemoteMachine
        """
        if not self._machine:
            raise Exception('sqlhosts未设置machine')
        return self._machine

    @machine.setter
    def machine(self, machine):
        self._machine = machine

    # @property
    # def session(self):
    #     """
    #     返回操作当前实例的SSHSession
    #     :return: SSHSession
    #     """
    #     return self._product.session

    def get_port(self, server_name):
        """
        获取指定实例的端口号
        :param server_name: str, server name
        :return: int
        """
        _port = None
        if server_name in self.server_entries:
            _port = self.server_entries.get(server_name).servicename
        else:
            for group_entry in self.group_entries.values():
                if server_name in group_entry.server_entries:
                    _port = group_entry.server_entries.get(server_name).servicename
                    break
        if not _port:
            raise Exception(f'Not found server <{server_name}>')
        return _port

    def get_ip(self, server_name):
        """
        获取指定server的ip
        :param server_name: str, server name
        :return: str
        """
        _ip = None
        if server_name in self.server_entries:
            _ip = self.server_entries.get(server_name).hostname
        else:
            for group_entry in self.group_entries.values():
                if server_name in group_entry.server_entries:
                    _ip = group_entry.server_entries.get(server_name).hostname
                    break
        if not _ip:
            raise Exception(f'Not found server <{server_name}>')
        return _ip

    def add_server_item(self, servername, hostname, port, connection_type: str = 'onsoctcp', **options):
        """
        添加一个自定义的server条目到当前sqlhosts
        :param servername: str, servername
        :param hostname: str, ip
        :param port: int, port
        :param connection_type: str, 连接类型
        :param options: dict，其他可选参数
        :return: None
        """
        server_entry = ServerEntry(servername, hostname, port, connection_type, **options)
        self.server_entries[server_entry.name] = server_entry

    def add_server(self, server: Server, connection_type: str = 'onsoctcp', **options):
        """
        添加server到sqlhosts
        :param servername: str, server名称
        :param ip: str, ip
        :param port: int, port
        :return:
        """
        server_entry = ServerEntry(server.name, server.ip, server.port, connection_type, **options)
        self.server_entries[server_entry.name] = server_entry

    def get_group_entry(self, name, **options) -> GroupEntry:
        """
        从sqlhosts中获取一个group entry
        :param name: 组名
        :param options: 可选参数(不包含i)
        :return: GroupEntry
        """
        if 'i' in options:
            options.pop('i')
        if name in self._group_entries:
            self._group_entries[name].options.update(options)
        else:
            group_entry = GroupEntry(name, self.group_number, **options)
            self._group_entries[group_entry.name] = group_entry
            self.group_number += 1
        return self._group_entries[name]

    def add_group_entry(self, group_entry: GroupEntry):
        """
        添加group entry到当前sqlhosts
        :param group_entry: GroupEntry
        :return: None
        """
        group_entry_copy = group_entry.copy()
        group_entry_copy.options.update({'i': self.group_number})
        self._group_entries[group_entry_copy.name] = group_entry_copy
        self.group_number += 1

    def to_file(self):
        """
        将sqlhosts对象转为文件
        :return: None
        """
        code, out = self.machine.run_cmd(f"rm -rf {self.path};touch {self.path}")
        if code != 0:
            raise Exception(f"创建sqlhosts文件失败，错误码{code}, 错误信息{out}")
        self.machine.run_cmd(f"echo '{str(self)}' >> {self.path}")
        self.machine.run_cmd(f"chmod 755 {self.path}")

    def load_file(self):
        """
        通过sqlhosts文件生成sqlhosts对象
        :return: None
        """
        code, out = self.machine.run_cmd(f"cat {self.path}")
        if code != 0:
            raise Exception(f"读取sqlhosts文件失败，错误码{code}, 错误信息{out}")
        self.server_entries.clear()
        self.group_entries.clear()
        for line in str(out).splitlines():
            line = line.strip()
            if line == '':
                continue
            items = line.split()
            if len(items) < 4:
                raise Exception(f'sqlhosts文件格式错误！error line context: "{line}"')
            if items[1] == 'group':
                options = {s.split('=')[0]:s.split('=')[1] for s in items[4].split(',')}
                group_num = options.pop('i')
                group_entry = GroupEntry(name=items[0], i=group_num,**options)
                self.group_entries[items[0]] = group_entry
            else:
                server_entry = ServerEntry(servername=items[0],  connection_type=items[1],hostname=items[2], port=int(items[3]))
                if len(items) == 5:
                    options = {s.split('=')[0]: s.split('=')[1] for s in items[4].split(',')}
                    server_entry.options.update(options)
                    group_name = options.get('g')
                    if group_name:
                        self.group_entries.get(group_name).add_server_entry(server_entry)
                    else:
                        self.server_entries[items[0]] = server_entry
                else:
                    self.server_entries[items[0]] = server_entry


    def remove_server_entry(self, server_name):
        """
        从sqlhosts中移除指定名称的server entry
        :param server_name: str
        :return:
        """
        if server_name in self.server_entries:
            self.server_entries.pop(server_name)

    def remove_group_entry(self, group_name):
        """
        从sqhosts中移除指定名称的group entry
        :param group_name: str
        :return:
        """
        if group_name in self.group_entries:
            self.group_entries.pop(group_name)

    def clear(self):
        """
        清空当前sqlhosts
        :return:
        """
        self.server_entries.clear()
        self.group_entries.clear()
        self._group_number = 1

    def extend(self, sqlhosts: SqlHosts):
        """
        将另一个sqlhosts的内容合并到当前sqlhosts
        :param sqlhosts: SqlHosts
        :return: None
        """
        sqlhosts_copy = sqlhosts.copy()
        self.server_entries.update(sqlhosts_copy.server_entries)
        self.group_entries.update(sqlhosts_copy.group_entries)
        for index, group_entry in enumerate(self.group_entries.values(), start=1):
            group_entry.number = index

    def copy(self) -> SqlHosts:
        """
        生成当前sqlhosts的副本
        :return:
        """
        new_sqlhosts = SqlHosts(path=None, machine=None)
        new_sqlhosts.server_entries.update(self.server_entries)
        new_sqlhosts.group_entries.update({group_name: group_entry.copy()
                                           for group_name, group_entry in self.group_entries.items()})
        return new_sqlhosts

    def __str__(self):
        group_text = "\n\n".join([str(group_entry) for group_entry in self.group_entries.values()])
        server_text = "\n".join([str(server_entry) for server_entry in self.server_entries.values()])
        if group_text.strip() == '':
            return server_text
        return "\n\n".join([group_text, server_text])
