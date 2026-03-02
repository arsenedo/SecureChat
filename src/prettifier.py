def bytes_to_string_bits(bytes_to_format):
    bytes_string = ""

    for byte in bytes_to_format:
        bytes_string += format(byte, "08b") + " "

    return bytes_string.strip()