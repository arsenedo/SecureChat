from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder

class SetMessageToBuffer(ICommand):
    def __init__(self, user_input: str):
        split_input = user_input.split(" ")

        if len(split_input) != 2:
            raise Exception("Incorrect input format")

        self.buffer = split_input[0]
        self.message = split_input[1]

    def execute(self, tcp_client, encoder):
        match self.buffer:
            case "plain":
                encoder.set_plain_buffer(self.message)
            case "encoded":
                encoder.set_encoded_buffer(self.message)