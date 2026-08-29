from thefuck.utils import for_app
from thefuck.specific.brew import match_brew_subcommand


@for_app('brew', at_least=2)
def match(command):
    return match_brew_subcommand(
        command, ['ln', 'link'], "brew link --overwrite --dry-run")


def get_new_command(command):
    command_parts = command.script_parts[:]
    command_parts[1] = 'link'
    command_parts.insert(2, '--overwrite')
    command_parts.insert(3, '--dry-run')
    return ' '.join(command_parts)
