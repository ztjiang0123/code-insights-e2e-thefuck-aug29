from thefuck.utils import replace_argument_from_output, for_app


@for_app('cargo', at_least=1)
def match(command):
    return ('no such subcommand' in command.output.lower()
            and 'Did you mean' in command.output)


def get_new_command(command):
    return replace_argument_from_output(
        command, r'Did you mean `([^`]*)`')
