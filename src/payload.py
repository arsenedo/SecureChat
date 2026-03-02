from enum import Enum

class PayloadType(Enum):
    TEXT = b"t"
    SERVER_TEXT = b"s"
    IMAGE = b"i"

class Payload:
    def __init__(
            self, 
            header: bytes, 
            msg_type: bytes,
            length: bytes, 
            message: bytes
        ):
        self.header = header
        self.msg_type = msg_type
        self.length = length
        self.message = message

    def to_byte_string(self):
        return self.header + self.msg_type + self.length + self.message