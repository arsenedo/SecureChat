import re
from cli.cli_command import ParsedCLICommand

def parse_cli_command(cli_command: str):
    found_command = re.search("^\/(\w+)(?:\s*-(\w))?(?:\s*([\w\W]+))?$", cli_command)

    # if doesn't contain a "/" at the start, count as text
    if not found_command:
        return ParsedCLICommand("send", user_input = cli_command)
    
    
    return ParsedCLICommand(found_command.group(1), found_command.group(2), found_command.group(3))