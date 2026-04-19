import re
from cli.cli_command import ParsedCLICommand
from payload import PayloadType

def parse_cli_command(cli_command: str):
    # group 1 -> alias, group 2 -> flags, group 3 -> user_input
    found_command = re.search(r"^\/(\w+)(?:\s*-(\w))?(?:\s*([\w\W]+))?$", cli_command)

    # if doesn't contain a "/" at the start, count as text
    if not found_command:
        return ParsedCLICommand("send", PayloadType.TEXT, user_input = cli_command)
    
    command_type: PayloadType = None
    match found_command.group(2):
        case "s":
            command_type = PayloadType.SERVER_TEXT
        case "t":
            command_type = PayloadType.TEXT
        case "i":
            command_type = PayloadType.IMAGE
        case _:
            command_type = PayloadType.TEXT

    alias = found_command.group(1)
    sub_type: str = None
    user_input: str = found_command.group(3)
    if (alias == "encode" or alias == "decode"):
        split_input = user_input.split(" ", 1)
        sub_type = split_input[0]
        user_input = split_input[1]
    
    return ParsedCLICommand(alias, command_type, user_input, sub_type)