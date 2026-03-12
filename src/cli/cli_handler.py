from cli import cli_controller, cli_model, cli_view
from cli.cli_command import CLICommand

class CLIHandler:
    def __init__(self):
        view = cli_view.CLIView()

        model = cli_model.CLIModel(view)
        model.set_cli_commands(self.get_cli_commands())

        self.controller = cli_controller.CLIController(model)

    def execute_cli_command(self, command: str):
        self.controller.parse_cli_command(command)
        
    def get_cli_commands(self):
        return [
            CLICommand(["help"])
        ]