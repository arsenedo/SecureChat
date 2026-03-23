import socket
from payload_builder import PayloadBuilder
from payload import *

class Client:
    s: socket.socket = None
    payload_builder: PayloadBuilder = None
    payload_history: list[Payload] = []

    def __init__(self, bytes_per_char = 4):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.payload_builder = PayloadBuilder(bytes_per_char)
    
    def connect(self, IP_address: str, port: int):
        self.s.connect((IP_address, port))

    def send(self, message: str, msg_type: PayloadType):
        payload: Payload = self.payload_builder.create(msg_type, message)
        self.s.send(payload.to_byte_string())

    def receive(self):
        payload_bytes = self.s.recv(4096)

        payload: Payload = self.payload_builder.parse(payload_bytes)

        self.payload_history.append(payload)

        return payload

    def close(self):
        self.s.close()