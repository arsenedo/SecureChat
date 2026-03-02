from payload import *

class PayloadBuilder:
    header = b"ISC"
    length_field_size = 2
    message_encoding = "utf-32-be"

    def __init__(self, bytes_per_char: int):
        self.bytes_per_char = bytes_per_char
        print(self.header)

    def create(
            self, 
            type: PayloadType, 
            message: str, 
            ):
        length = (len(message) * self.bytes_per_char).to_bytes(self.length_field_size)
        encoded_message = message.encode(self.message_encoding)
        
        return Payload(self.header, type.value, length, encoded_message)
    
    def parse(payload_bytes: bytes):
        header = payload_bytes[0:3]
        msg_type = payload_bytes[3:4]
        msg_length = payload_bytes[4:6]
        msg = payload_bytes[6: 6 + msg_length]

        return Payload(
            header, 
            msg_type, 
            msg_length, 
            msg
        )