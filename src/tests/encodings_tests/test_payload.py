import payload_builder, prettifier
from payload_builder import *

def test_encode_message():
    message = "test"

    encoded_message = PayloadBuilder.encode_message(message)
    
    decoded_message = encoded_message.decode("utf-32-be")

    assert message == decoded_message

def test_encode_multibyte_char():
    message = "Ω" # takes 2 bytes

    encoded_message = PayloadBuilder.encode_message(message)

    ## encoder should only add 2 padding bytes
    assert prettifier.bytes_to_string_bits(encoded_message) == "00000000 00000000 11001110 10101001"