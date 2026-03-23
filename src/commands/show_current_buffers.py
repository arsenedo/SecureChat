from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder
from cli.cli_view import CLIView

class ShowCurrentBuffers(ICommand):
    def __init__(self, cli_view: CLIView):
        self.cli_view = cli_view
        
    def execute(self, tcp_client: Client, encoder: Encoder):
        self.cli_view.print_string(f"Plain : {encoder.plain_buffer}")
        self.cli_view.print_string(f"Encoded : {encoder.encoded_buffer}")