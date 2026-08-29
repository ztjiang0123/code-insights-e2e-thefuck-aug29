import subprocess
from ..utils import memoize, which


brew_available = bool(which('brew'))


@memoize
def get_brew_path_prefix():
    """To get brew path"""
    try:
        return subprocess.check_output(['brew', '--prefix'],
                                       universal_newlines=True).strip()
    except Exception:
        return None


def match_brew_subcommand(command, subcommands, output_hint):
    """Shared matcher for ``brew`` rules that suggest a corrected subcommand.

    :type command: thefuck.types.Command
    :param subcommands: subcommand names the second script part may use
    :param output_hint: substring brew prints when hinting the correction
    :rtype: bool

    """
    return (command.script_parts[1] in subcommands
            and output_hint in command.output)
