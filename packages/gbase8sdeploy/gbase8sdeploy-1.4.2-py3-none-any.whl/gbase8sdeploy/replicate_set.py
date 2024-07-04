# coding: utf-8
# @Author:  wangwei
from gbase8sdeploy.replicate import Replicate


class ReplicateSet:
    auto_id = 0

    def __init__(self, er_domain, name: str = None):
        self._er_domain = er_domain
        if not name:
            self._name = 'replset_' + str(ReplicateSet.get_auto_id())
        else:
            self._name = name
        self._defined = False
        self._started = False
        self._suspended = False
        self._frequency_opt: Replicate.FrequencyOption = None
        self._frequency_time = None
        self._exclusive = False
        self._define_cmd = None

    @property
    def define_cmd(self):
        return self._define_cmd

    @property
    def name(self):
        return self._name

    @staticmethod
    def get_auto_id():
        ReplicateSet.auto_id += 1
        return ReplicateSet.auto_id

    def set_frequency(self, frequency_opt: Replicate.FrequencyOption, frequency_time: str = None):
        self._frequency_opt = frequency_opt
        self._frequency_time = frequency_time

    def get_frequency_cmd(self):
        cmd = ""
        if self._frequency_opt:
            if self._frequency_opt == Replicate.FrequencyOption.IMMEDIATE:
                cmd += f' --{self._frequency_opt.value}'
            elif self._frequency_opt in (Replicate.FrequencyOption.INTERVAL, Replicate.FrequencyOption.ATTIME):
                if self._frequency_time:
                    cmd += f' --{self._frequency_opt.value}={self._frequency_time}'
                else:
                    raise Exception('INTERVAL和ATTIME频率处理方式必须指定频率时间')
        return cmd

    def set_exclusive(self, v: bool):
        self._exclusive = v

    def get_exclusive_cmd(self):
        cmd = ""
        if self._exclusive:
            cmd += " --exclusive"
        return cmd

    def add_replicate(self, replicate: Replicate):
        if self._defined:
            self.change(self._er_domain.root_node, Replicate.ChangeReplOption.ADD, replicate)

    def startup(self):
        """
        启动复制
        :return: None
        """
        if self._started:
            raise Exception(f'replicate {self.name} already started')
        else:
            code, out = self._er_domain.root_node.run_cmd(f'cdr start replicateset {self.name}')
            if code != 0:
                raise Exception(f'启动replicate set {self.name}失败，错误码：{code}, 错误信息{out}')
            else:
                self._started = True

    def shutdown(self):
        """
        停止复制
        :return: None
        """
        self._er_domain.root_node.server.run_cmd(f'cdr stop replicateset {self.name}')
        self._started = False

    def define(self):
        """
        定义复制集
        :return: None
        """
        define_cmd = f"cdr define replicateset {self.name}"
        define_cmd += self.get_frequency_cmd()
        define_cmd += self.get_exclusive_cmd()
        self._define_cmd = define_cmd
        code, out = self._er_domain.root_node.run_cmd(define_cmd)
        if code != 0:
            raise Exception(f'执行{define_cmd}失败，错误码：{code}, 错误信息：{out}')
        self._defined = True

    def change(self, er_node, change_repl_option: Replicate.ChangeReplOption, replicate: Replicate):
        """
        """
        cmd = 'cdr change replicateset'
        if not self._defined:
            raise Exception(f'ReplicateSet: {self.name} - 因为还没有定义所以不能change')
        cmd += f" --{change_repl_option.value}"
        cmd += f" {self.name} {replicate.name}"
        code, out = er_node.run_cmd(cmd)
        if code != 0:
            raise Exception(f"执行{cmd}失败, 错误码：{code}, 错误信息: {out}")
