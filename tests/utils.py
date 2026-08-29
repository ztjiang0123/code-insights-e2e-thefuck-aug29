from thefuck import types
from thefuck.const import DEFAULT_PRIORITY


class Rule(types.Rule):
    def __init__(self, name='', match=lambda *_: True,
                 get_new_command=lambda *_: '',
                 enabled_by_default=True,
                 side_effect=None,
                 priority=DEFAULT_PRIORITY,
                 requires_output=True):
        # `Rule.from_path` builds instances via ``cls(RuleSpec(...))``; accept
        # that spec directly so the ergonomic keyword form below stays optional.
        if isinstance(name, types.RuleSpec):
            spec = name
        else:
            spec = types.RuleSpec(
                name=name,
                match=match,
                get_new_command=get_new_command,
                enabled_by_default=enabled_by_default,
                side_effect=side_effect,
                priority=priority,
                requires_output=requires_output)
        super(Rule, self).__init__(spec)


class CorrectedCommand(types.CorrectedCommand):
    def __init__(self, script='', side_effect=None, priority=DEFAULT_PRIORITY):
        super(CorrectedCommand, self).__init__(
            script, side_effect, priority)
