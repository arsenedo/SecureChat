import encoder, prettifier

def test_encode_word():
    word = "hello"
    key = "python"

    xor_string = prettifier.bytes_to_string_bits(encoder.xor(word, key))

    assert xor_string == "00011000 00011100 00011000 00000100 00000000"

def test_encode_string():
    string = "hello world"
    key = "python"

    xor_string = prettifier.bytes_to_string_bits(encoder.xor(string, key));

    assert xor_string == "00011000 00011100 00011000 00000100 00000000 01001110 00000111 00010110 00000110 00000100 00001011"