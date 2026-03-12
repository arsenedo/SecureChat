from cli import cli_model

class CLIController:
    def __init__(self, cli_model: cli_model.CLIModel):
        self.cli_model = cli_model

    def parse_cli_command(self, cli_command: str):
        print(f"requested execute: {cli_command}")
        pass