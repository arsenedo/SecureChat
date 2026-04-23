def bytify_string(string: str, byte_length: int = 4) -> bytes :
    bytes_array = bytearray()

    for char in string:
        bytified_char = int.from_bytes(char.encode("utf-8"), "big").to_bytes(byte_length, "big")

        bytes_array.extend(bytified_char)
    
    return bytes(bytes_array)