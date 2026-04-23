from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder
from encoder import difhel_half_key, difhel_secret
from cli.cli_view import CLIView

class GenerateHalfKeyCommand(ICommand):
    def __init__(self, user_input: str, cli_view: CLIView):
        self.cli_view = cli_view

        split_input = user_input.split(" ")

        self.mod = int(split_input[0])
        self.gen = int(split_input[1])
        self.private_key = int(split_input[2])
    
    def execute(self, tcp_client: Client, encoder: Encoder):
        self.cli_view.print_string(f"Your halfkey is : {difhel_half_key(self.mod, self.gen, self.private_key)}")

class CalculateDifHelSecretCommand(ICommand):
    def __init__(self, user_input: str, cli_view: CLIView):
        self.cli_view = cli_view

        split_input = user_input.split(" ")

        self.mod = int(split_input[0])
        self.private_key = int(split_input[1])
        self.partner_half_key = int(split_input[2])

    def execute(self, tcp_client, encoder):
        self.cli_view.print_string(f"The secret is : {difhel_secret(self.mod, self.private_key, self.partner_half_key)}")

        