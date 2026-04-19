from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder, vigenere_encode, vigenere_decode
from utils.bytes_utils import bytify_string

class VigenereCommand(ICommand):
    def __init__(self, user_input: str, is_encode: bool):
        self.is_encode = is_encode
        self.key = bytify_string(user_input, 4)

    def execute(self, tcp_client: Client, encoder: Encoder):
        if self.is_encode:
            encoder.set_encoded_buffer(vigenere_encode(
                encoder.plain_buffer, 
                self.key
            ))
        else:
            encoder.set_plain_buffer(vigenere_decode(
                encoder.encoded_buffer,
                -self.key
            ))