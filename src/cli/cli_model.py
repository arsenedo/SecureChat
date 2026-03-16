from cli.cli_view import CLIView
from cli.cli_command import CLICommand
import os

class CLIModel:
    def __init__(self, view: CLIView):
        self.cli_view = view
        view.print_header()

    def execute_parsed_command(self, parsed_command: str):
        command = next((cli_command for cli_command in self.get_cli_commands() if parsed_command in cli_command.aliases), None)

        if not command:
            self.cli_view.print_string(f"Command {parsed_command} not found")
            return

        command.execute()

    def get_cli_commands(self):
        return [
            CLICommand(
                aliases = ["help"], 
                callback = lambda : self.cli_view.print_available_commands(self.get_cli_commands())
            ),
            CLICommand(
                aliases = ["quit", "exit", "q"], 
                callback = lambda : os._exit(0)
            )
        ]
