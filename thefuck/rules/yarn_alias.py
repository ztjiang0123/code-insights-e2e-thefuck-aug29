from thefuck.utils import replace_argument_from_output, for_app


@for_app('yarn', at_least=1)
def match(command):
    return 'Did you mean' in command.output


def get_new_command(command):
    return replace_argument_from_output(
        command, r'Did you mean [`"](?:yarn )?([^`"]*)[`"]')
