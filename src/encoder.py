import utils.array_utils as array_utils

class Encoder:
    plain_buffer: bytes = bytes()
    encoded_buffer: bytes = bytes()

    def clear_plain_buffer(self):
        self.plain_buffer = bytes()

    def clear_encoded_buffer(self):
        self.encoded_buffer = bytes()

    def set_plain_buffer(self, bytes_text: bytes):
        self.plain_buffer = bytes_text

    def set_encoded_buffer(self, bytes_text: bytes):
        self.encoded_buffer = bytes_text

def caesar_shift(encoded_bytes: bytes, shift: int):
    result = bytearray()

    for i in range(0, len(encoded_bytes), 4):
        shifted = int.from_bytes(encoded_bytes[i:i+4]) + shift

        result.extend(shifted.to_bytes(4, "big"))

    return bytes(result)

def xor(string, key):
    len_adjusted_key = array_utils.adjust_key_length(key, len(string))

    stringBytes = bytes(string, "utf-8")
    keyBytes = bytes(len_adjusted_key, "utf-8")
    
    encodeTuple = zip(stringBytes, keyBytes)
    
    xorArray = []
    for pair in encodeTuple:
        xor = pair[0] ^ pair[1]

        xorArray.append(xor)
    
    xorBytes = bytes(xorArray)

    return xorBytes

def vigenere_encode(str_bytes: bytes, key_bytes: bytes):
    len_adjusted_key = array_utils.adjust_key_length(key_bytes, len(str_bytes))

    encrypted_bytes: bytearray = bytearray()
    for i in range(0, len(str_bytes), 4):
        int_char = int.from_bytes(str_bytes[i: i+4])
        int_key = int.from_bytes(len_adjusted_key[i: i+4])

        int_encrypted = int_char + int_key
        encrypted_bytes.extend(int_encrypted.to_bytes(4, "big"))

    return bytes(encrypted_bytes)

def vigenere_decode(encoded_msg: bytes, key_bytes: bytes):
    len_adjusted_key = array_utils.adjust_key_length(key_bytes, len(encoded_msg))

    decrypted_bytes: bytearray = bytearray()
    for i in range(0, len(encoded_msg), 4):
        int_char = int.from_bytes(encoded_msg[i: i+4])
        int_key = int.from_bytes(len_adjusted_key[i: i+4])

        int_decrypted = int_char - int_key

        decrypted_bytes.extend(int_decrypted.to_bytes(4, "big"))

    return bytes(decrypted_bytes)


def rsa_encode(encoded_msg: bytes, n: int, e: int) -> bytes:
    encrypted_bytes: bytearray = bytearray()
    for i in range(0, len(encoded_msg), 4):
        int_char: int = int.from_bytes(encoded_msg[i: i + 4])
        int_encoded: int = (int_char ** e) % n

        encrypted_bytes.extend(int_encoded.to_bytes(4, "big"))

    return bytes(encrypted_bytes)