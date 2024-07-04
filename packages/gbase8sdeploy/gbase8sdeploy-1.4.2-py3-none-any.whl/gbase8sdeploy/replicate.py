# coding: utf-8
# @Author:  wangwei
from enum import Enum


class Replicate:
    auto_id = 0

    class ConflictOption(Enum):
        TIMESTAMP = 'timestamp'
        ALWAYS = 'always'
        DELETEWINS = 'deletewins'
        SPLROUTINE = 'splroutine'
        IGNORE = 'ignore'

    class ScopeOption(Enum):
        TRANSACTION = 'transaction'
        ROW = 'row'

    class FrequencyOption(Enum):
        IMMEDIATE = 'immed'
        INTERVAL = 'every'
        ATTIME = 'at'

    class FloatOption(Enum):
        NONE = ''
        IEEE = 'floatieee'
        CANONICAL = 'floatcanon'

    class ParticipantType(Enum):
        UPDATE_ANYWHERE = ''
        PRIMARY = 'P '
        TARGET = 'R '
        SENDONLY = 'S '

    class OwnerOption(Enum):
        NONE = ''
        OWNER = 'O '
        GBASEDBT = 'I '

    class ChangeReplOption(Enum):
        ADD = 'add'
        DELETE = 'del'

    def __init__(self, er_domain, name: str = None):
        self._er_domain = er_domain
        if not name:
            self._name = 'repl_' + str(Replicate.get_auto_id())
        else:
            self._name = name
        self._conflict_opt: Replicate.ConflictOption = Replicate.ConflictOption.TIMESTAMP
        self._conflict_spl = None
        self._scope_opt: Replicate.ScopeOption = None
        self._frequency_opt: Replicate.FrequencyOption = Replicate.FrequencyOption.IMMEDIATE
        self._frequency_time = None
        self._float_opt: Replicate.FloatOption = Replicate.FloatOption.IEEE
        self._activate_ats = True
        self._activate_ris = True
        self._replicate_fullrow = False
        self._ignore_del = False
        self._primarykey = False
        self._is_classic_replicate = False
        self._fire_trigger = False
        self._defined = False
        self._started = False
        self._suspended = False
        self._er_key = False
        self._conflict_spl_routine_optimized = False
        self._define_cmd = None

    @property
    def define_cmd(self):
        return self._define_cmd

    @property
    def name(self):
        return self._name

    @staticmethod
    def get_auto_id():
        Replicate.auto_id += 1
        return Replicate.auto_id

    def set_classic(self, v: bool):
        self._is_classic_replicate = v

    def get_classic_cmd(self):
        cmd = ""
        if self._is_classic_replicate:
            cmd += " --classic"
        return cmd

    def set_fire_trigger(self, v: bool):
        self._fire_trigger = v

    def get_fire_trigger_cmd(self):
        cmd = ""
        if self._fire_trigger:
            cmd += "  firetrigger"
        return cmd

    def set_primarykey(self, v: bool):
        self._primarykey = v

    def get_primarykey_cmd(self):
        cmd = ""
        if self._primarykey:
            cmd += " -K"
        return cmd

    def set_er_key(self, v: bool):
        self._er_key = v

    def get_er_key_cmd(self):
        cmd = ""
        if self._er_key:
            cmd += " --erkey"
        return cmd

    def set_conflict(self, conflict_opt: ConflictOption, conflict_spl_routine: str = None, optimized=False):
        self._conflict_opt = conflict_opt
        if self._conflict_opt == Replicate.ConflictOption.SPLROUTINE:
            if not conflict_spl_routine:
                raise Exception('SPLROUTINE冲突处理方式必须指定spl_routine')
            self._conflict_spl = conflict_spl_routine
            self._conflict_spl_routine_optimized = optimized

    def get_conflict_cmd(self):
        cmd = ""
        if self._conflict_opt != Replicate.ConflictOption.SPLROUTINE:
            cmd += f" --conflict={self._conflict_opt.value}"
        else:
            if self._conflict_spl:
                cmd += f' --conflict={self._conflict_spl}'
                if self._conflict_spl_routine_optimized:
                    cmd += ' --optimized'
            else:
                raise Exception('SPLROUTINE冲突处理方式必须指定spl_routine')
        return cmd

    def set_scope(self, scope_opt: ScopeOption):
        self._scope_opt = scope_opt

    def get_scope_cmd(self):
        cmd = ""
        if self._scope_opt:
            if self._scope_opt == Replicate.ScopeOption.TRANSACTION:
                cmd += f" --scope={self._scope_opt.TRANSACTION.value}"
            elif self._scope_opt == Replicate.ScopeOption.ROW:
                cmd += f' --scope={self._scope_opt.ROW.value}'
            else:
                raise Exception('不支持的scope, 请输入: ScopeOptions.(TRANSACTION|ROW)')
        return cmd

    def set_frequency(self, frequency_opt: FrequencyOption, frequency_time: str = None):
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

    def set_float(self, float_opt: FloatOption):
        self._float_opt = float_opt

    def get_float_cmd(self):
        cmd = ""
        if self._float_opt:
            if self._float_opt == Replicate.FloatOption.NONE:
                pass
            elif self._float_opt in (Replicate.FloatOption.IEEE, Replicate.FloatOption.CANONICAL):
                cmd += f" --{self._float_opt.value}"
            else:
                raise Exception('不支持的float, 请输入: FloatOptions.(NONE|IEEE|CANONICAL)')
        return cmd

    def set_ats(self, v: bool):
        self._activate_ats = v

    def get_ats_cmd(self):
        cmd = ""
        if self._activate_ats:
            cmd += ' --ats'
        return cmd

    def set_ris(self, v: bool):
        self._activate_ris = v

    def get_ris_cmd(self):
        cmd = ""
        if self._activate_ris:
            cmd += ' --ris'
        return cmd

    def set_fullrow(self, v: bool):
        self._replicate_fullrow = v

    def get_fullrow_cmd(self):
        cmd = ""
        if self._replicate_fullrow:
            cmd += ' --fullrow=y'
        return cmd

    def set_ignore_del(self, v: bool):
        self._ignore_del = v

    def get_ignore_del(self):
        cmd = ""
        if self._ignore_del:
            cmd += ' --ignoredel=y'
        else:
            cmd += ' --ignoredel=n'
        return cmd

    def add_participant(self, er_node, er_participant_node, db_name, tab_name, tab_owner, select_stmt,
                        participation_type: ParticipantType = ParticipantType.UPDATE_ANYWHERE,
                        owner_opt: OwnerOption = OwnerOption.NONE
                        ):
        """
        添加参与者
        :param er_node: ERNode, 执行命令的ER节点
        :param er_participant_node: ERNode, 参与者ER节点
        :param db_name: str, 数据库名称
        :param tab_name: str, 表名称
        :param tab_owner: str, 所有者
        :param select_stmt: str, 查询语句
        :param participation_type: ParticipantType，参与者类型
        :param owner_opt: OwnerOption， 用户权限检查
        :return: None
        """
        cmd = f'"{participation_type.value}{owner_opt.value}{db_name}@{er_participant_node.group_name}:{tab_owner}.{tab_name}" ' \
              f'"{select_stmt}"'
        if self._defined:
            self.change(er_node, Replicate.ChangeReplOption.ADD, cmd)

    def startup(self):
        """
        启动复制
        :return: None
        """
        if self._started:
            raise Exception(f'replicate {self.name} already started')
        else:
            code, out = self._er_domain.root_node.run_cmd(f'cdr start repl {self.name}')
            if code != 0:
                raise Exception(f'启动replicate {self.name}失败，错误码：{code}, 错误信息{out}')
            else:
                self._started = True

    def shutdown(self):
        """
        停止复制
        :return: None
        """
        self._er_domain.root_node.server.run_cmd(f'cdr stop repl {self.name}')
        self._started = False

    def define(self):
        """
        定义复制
        :return: None
        """
        define_cmd = f"cdr define replicate {self.name}"
        define_cmd += self.get_classic_cmd()
        define_cmd += self.get_conflict_cmd()
        define_cmd += self.get_scope_cmd()
        define_cmd += self.get_frequency_cmd()
        define_cmd += self.get_float_cmd()
        define_cmd += self.get_ats_cmd()
        define_cmd += self.get_ris_cmd()
        define_cmd += self.get_fire_trigger_cmd()
        define_cmd += self.get_fullrow_cmd()
        define_cmd += self.get_ignore_del()
        define_cmd += self.get_primarykey_cmd()
        define_cmd += self.get_er_key_cmd()
        self._define_cmd = define_cmd
        code, out = self._er_domain.root_node.run_cmd(define_cmd)
        if code != 0:
            raise Exception(f'执行{define_cmd}失败，错误码：{code}, 错误信息：{out}')
        self._defined = True

    def change(self, er_node, change_repl_option: ChangeReplOption, participant: str):
        """
        通过添加或删除一个或多个参与者，来修改当前复制
        :param er_node: ChangeReplOption
        :param change_repl_option:
        :param participant: str, ex. "db_name@group_name:tab_owner.tab_name" "select_stmt"
        :return: None
        """
        cmd = 'cdr change replicate'
        if not self._defined:
            raise Exception(f'Replicate: {self.name} - 因为还没有定义所以不能change')
        cmd += f" --{change_repl_option.value}"
        if self._er_key:
            cmd += " --erkey"
        cmd += f" {self.name} {participant}"
        code, out = er_node.run_cmd(cmd)
        if code != 0:
            raise Exception(f"执行{cmd}失败, 错误码：{code}, 错误信息: {out}")
