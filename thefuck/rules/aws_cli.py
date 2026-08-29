from thefuck.utils import for_app, get_valid_choices_command

INVALID_CHOICE = "(?<=Invalid choice: ')(.*)(?=', maybe you meant:)"
OPTIONS = "^\\s*\\*\\s(.*)"


@for_app('aws')
def match(command):
    return "usage:" in command.output and "maybe you meant:" in command.output


def get_new_command(command):
    return get_valid_choices_command(command, INVALID_CHOICE, OPTIONS)
