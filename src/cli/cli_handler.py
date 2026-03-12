from cli import cli_controller, cli_model, cli_view
from cli.cli_command import CLICommand

class CLIHandler:
    def __init__(self):
        view = cli_view.CLIView()

        model = cli_model.CLIModel(view)
        model.set_cli_commands(self.get_cli_commands())

        controller = cli_controller.CLIController(model)

    def get_cli_commands(self):
        return [
            CLICommand(["help"])
        ]