from payload import *

header = b"ISC"
length_field_size = 2
message_encoding = "utf-8"
bytes_per_char = 4

class PayloadBuilder:
    @staticmethod
    def create(
            type: PayloadType, 
            encoded_message: bytes, 
            ):

        length = int.to_bytes(len(encoded_message) // 4, 2, "big")
        
        return Payload(header, type.value, length, encoded_message)
    
    @staticmethod
    def parse(payload_bytes):
        header = payload_bytes[0:3]
        msg_type = payload_bytes[3:4]
        msg_length = int.from_bytes(payload_bytes[4:6], "big") * bytes_per_char
        msg = payload_bytes[6: 6 + msg_length]

        return Payload(
            header, 
            msg_type, 
            msg_length, 
            msg
        )
    
    @staticmethod
    def encode_message(string: str):
        padding = int.to_bytes(0, 1, "big")

        bytes_message = bytes()

        for char in string:
            encoded_char = char.encode(message_encoding)
            bytes_message += padding * (bytes_per_char - len(encoded_char))
            bytes_message += encoded_char

        return bytes_message