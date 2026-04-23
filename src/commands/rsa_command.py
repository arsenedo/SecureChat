from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder, rsa_encode, rsa_decode

class RSACommand(ICommand):
    def __init__(self, user_input: str, is_encode: bool):
        self.is_encode = is_encode

        split_input = user_input.split(" ")
        self.key: int = int(split_input[0]) # public if is_encode = True else private
        self.mod: int = int(split_input[1])

    
    def execute(self, tcp_client: Client, encoder: Encoder):
        if self.is_encode:
            encoder.set_encoded_buffer(rsa_encode(
                    encoder.plain_buffer,
                    self.mod,
                    self.key
                ))
        else:
            encoder.set_encoded_buffer(rsa_decode(
                encoder.plain_buffer,
                self.mod,
                self.key
            ))