from cli import cli_model, cli_view, cli_command
from commands.command_invoker import CommandInvoker
import utils.cli_utils as cli_utils
import re

class CLIHandler:
    def __init__(self, command_invoker: CommandInvoker):
        view = cli_view.CLIView()

        self.model = cli_model.CLIModel(view, command_invoker)

    def execute_cli_command(self, command: str):
        parsed_command: cli_command.ParsedCLICommand = cli_utils.parse_cli_command(command)

        self.model.execute_parsed_command(parsed_command)