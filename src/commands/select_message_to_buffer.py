from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder

class SelectMessageToBuffer(ICommand):
    def __init__(self, user_input: str):
        self.user_input = user_input if user_input != None else ""

    def execute(self, tcp_client: Client, encoder: Encoder):
        params = self.user_input.split(" ")
        if len(params) != 2:
            print("Not enough parameters provided")
            return
        
        message_id = int(params[0])
        buffer = params[1]

        payload = tcp_client.payload_history[message_id - 1]

        if buffer == "e":
            encoder.set_encoded_buffer(payload.message)
        elif buffer == "c":
            encoder.set_plain_buffer(payload.message)
        else:
            print("Please specify a valid buffer")

