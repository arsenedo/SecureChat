from commands.command_invoker import ICommand
from payload import PayloadType
from client import Client
from encoder import Encoder

class SendTextCommand(ICommand):
    def __init__(self, msg: str, payload_type: PayloadType):
        self.msg = msg
        self.payload_type = payload_type

    def execute(self, tcp_client: Client, encoder: Encoder):
        msg_to_send = self.msg

        match self.msg:
            case "plain":
                msg_to_send = encoder.plain_buffer
            case "encoded":
                msg_to_send = encoder.encoded_buffer

        tcp_client.send(msg_to_send, self.payload_type)