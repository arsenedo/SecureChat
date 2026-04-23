from commands.command_invoker import ICommand
from payload import *
from payload_builder import PayloadBuilder
from client import Client
from encoder import Encoder

class SendTextCommand(ICommand):
    def __init__(self, msg: str, payload_type: PayloadType):
        self.msg = msg
        self.payload_type = payload_type

    def execute(self, tcp_client: Client, encoder: Encoder):
        match self.msg:
            case "plain":
                msg_to_send = encoder.plain_buffer
            case "encoded":
                msg_to_send = encoder.encoded_buffer
            case _:
                msg_to_send = PayloadBuilder.encode_message(self.msg)

        payload: Payload = PayloadBuilder.create(self.payload_type, msg_to_send)

        tcp_client.send(payload)