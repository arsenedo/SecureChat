from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder

class SelectMessageToBuffer(ICommand):
    def __init__(self, user_input: str):
        self.message_id = int(user_input)

    def execute(self, tcp_client: Client, encoder: Encoder):
        payload = tcp_client.payload_history[self.message_id - 1]
        message = payload.message.decode("utf-8")

        encoder.set_plain_buffer(message)
        encoder.set_encoded_buffer(message)