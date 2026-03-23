from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder

class CaesarShiftCommand(ICommand):
    def __init__(self, user_input: str, is_encode: bool):
        self.is_encode = is_encode
        self.shift = int(user_input.split(" ")[1])

    
    def execute(self, tcp_client, encoder):
        if self.is_encode:
            encoder.encode_shift(self.shift)
        else:
            encoder.decode_shift(self.shift)