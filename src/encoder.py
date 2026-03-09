import utils

def caesar_shift(string: str, shift: int):
    result = ""
    for char in string:
        shifted = chr(ord(char) + shift)

        result += shifted
    return result

def xor(string, key):
    len_adjusted_key = utils.adjust_key_length(key, len(string))

    stringBytes = bytes(string, "utf-8")
    keyBytes = bytes(len_adjusted_key, "utf-8")
    
    encodeTuple = zip(stringBytes, keyBytes)
    
    xorArray = []
    for pair in encodeTuple:
        xor = pair[0] ^ pair[1]

        xorArray.append(xor)
    
    xorBytes = bytes(xorArray)

    return xorBytes

def vigenere_encode(string: str, key_string: str):
    len_adjusted_key = utils.adjust_key_length(key_string, len(string))

    string_chars = list(string)
    key_string_chars = list(len_adjusted_key)

    encode_tuple = zip(string_chars, key_string_chars)

    encrypted_string = ""
    for char, key in encode_tuple:
        print(ord(char) + ord(key), end=" ")
        encrypted_bytes = (ord(char) + ord(key))

        encrypted_string += chr(encrypted_bytes)

    return encrypted_string

def vigenere_decode(encoded_msg: str, key_string: str):
    len_adjusted_key = utils.adjust_key_length(key_string, len(encoded_msg))

    msg_chars = list(encoded_msg)
    key_string_chars = list(len_adjusted_key)

    decode_tuple = zip(msg_chars, key_string_chars)

    decrypted_string = ""
    for char, key in decode_tuple:
        print(char, key)
        decrypted_bytes = ord(char) - ord(key)

        decrypted_string += chr(decrypted_bytes)

    return decrypted_string
