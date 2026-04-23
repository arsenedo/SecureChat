from client import Client
from encoder import Encoder

class ICommand:
    def execute(self, tcp_client: Client, encoder: Encoder):
        raise NotImplementedError("You must implement the execute method")

class CommandInvoker:
    _command: ICommand = None

    def __init__(self, tcp_client, encoder):
        self._tcp_client = tcp_client
        self._encoder = encoder

    def set_command(self, command):
        self._command = command

    def execute_command(self):
        if not self._command:
            raise Exception("No command assigned to the Invoker")
        self._command.execute(self._tcp_client, self._encoder)