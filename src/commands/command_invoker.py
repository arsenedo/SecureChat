from client import Client

class ICommand:
    def execute(self, tcp_client: Client):
        raise NotImplementedError("You must implement the execute method")

class CommandInvoker:
    _command: ICommand = None

    def __init__(self, tcp_client):
        self._tcp_client = tcp_client

    def set_command(self, command):
        self._command = command

    def execute_command(self):
        if not self._command:
            raise 
        self._command.execute(self._tcp_client)