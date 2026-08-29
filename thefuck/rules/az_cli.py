from thefuck.utils import for_app, get_valid_choices_command

INVALID_CHOICE = "(?=az)(?:.*): '(.*)' is not in the '.*' command group."
OPTIONS = "^The most similar choice to '.*' is:\n\\s*(.*)$"


@for_app('az')
def match(command):
    return "is not in the" in command.output and "command group" in command.output


def get_new_command(command):
    return get_valid_choices_command(command, INVALID_CHOICE, OPTIONS,
                                     mistake_group=1)
