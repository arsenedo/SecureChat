from commands.command_invoker import ICommand
from client import Client
from encoder import Encoder
from hashlib import sha256

class HashCommand(ICommand):
    def execute(self, tcp_client: Client, encoder: Encoder):
        encoder.set_encoded_buffer(sha256(encoder.plain_buffer.decode("utf-32-be").encode("utf-8")).hexdigest().encode("utf-32-be"))