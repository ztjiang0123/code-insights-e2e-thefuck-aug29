from thefuck.utils import for_app
from thefuck.specific.brew import match_brew_subcommand


@for_app('brew', at_least=2)
def match(command):
    return match_brew_subcommand(
        command, ['uninstall', 'rm', 'remove'], "brew uninstall --force")


def get_new_command(command):
    command_parts = command.script_parts[:]
    command_parts[1] = 'uninstall'
    command_parts.insert(2, '--force')
    return ' '.join(command_parts)
