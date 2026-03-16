from cli import cli_model, cli_view
from cli.cli_command import CLICommand
import re

class CLIHandler:
    def __init__(self):
        view = cli_view.CLIView()

        self.model = cli_model.CLIModel(view)

    def execute_cli_command(self, command: str):
        parsed_command = self._parse_cli_command(command)

        self.model.execute_parsed_command(parsed_command)

    def _parse_cli_command(self, cli_command: str):
        found_command = re.search("\/(\w+)", cli_command)

        return found_command.group(1) if found_command else "unknown_command"