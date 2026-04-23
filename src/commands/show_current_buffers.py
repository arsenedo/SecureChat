from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder
from cli.cli_view import CLIView

class ShowCurrentBuffers(ICommand):
    def __init__(self, cli_view: CLIView, user_input: str):
        self.cli_view = cli_view
        self.user_input: str = user_input
        
    def execute(self, tcp_client: Client, encoder: Encoder):
        should_stringify = False
        if self.user_input:
            should_stringify = "stringify" in self.user_input.lower()

        self.cli_view.print_string(f"Plain : {encoder.plain_buffer if not should_stringify else encoder.plain_buffer.decode("utf-8", "replace")}")
        self.cli_view.print_string(f"Encoded : {encoder.encoded_buffer if not should_stringify else encoder.encoded_buffer.decode("utf-8", "replace")}")