from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder
from encoder import caesar_shift

class CaesarShiftCommand(ICommand):
    def __init__(self, user_input: str, is_encode: bool):
        self.is_encode = is_encode
        self.shift = int(user_input.split(" ")[1])

    
    def execute(self, tcp_client: Client, encoder: Encoder):
        if self.is_encode:
            encoder.set_encoded_buffer(caesar_shift(
                    encoder.plain_buffer, 
                    self.shift
                ))
        else:
            encoder.set_plain_buffer(caesar_shift(
                    encoder.encoded_buffer, 
                    -self.shift
                ))