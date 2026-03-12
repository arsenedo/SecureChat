from cli.cli_view import CLIView
from cli.cli_command import CLICommand

class CLIModel:
    cli_commands = []
    def __init__(self, view: CLIView):
        self.cli_view = view
        view.print_header()

    def set_cli_commands(self, commands: list[CLICommand]):
        commands = commands
