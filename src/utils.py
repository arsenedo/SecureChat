def adjust_key_length(key, msg_len):
    length_multiple = msg_len // len(key) + 1
    return (key * length_multiple)[:msg_len]