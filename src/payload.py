from enum import Enum

class PayloadType(Enum):
    TEXT = b"t"
    SERVER_TEXT = b"s"
    IMAGE = b"i"

class Payload:
    def __init__(
            self, 
            header: bytes, 
            type: bytes,
            length: bytes, 
            message: bytes
        ):
        self.header = header
        self.type = type
        self.length = length
        self.message = message

    def to_byte_string(self):
        return self.header + self.type.value + self.length + self.message