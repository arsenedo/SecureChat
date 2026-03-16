from commands.command_invoker import ICommand
from payload import PayloadType
from client import Client

class SendTextCommand(ICommand):
    def __init__(self, msg: str, payload_type: PayloadType):
        self.msg = msg
        self.payload_type = payload_type

    def execute(self, tcp_client: Client):
        tcp_client.send(self.msg, self.payload_type)