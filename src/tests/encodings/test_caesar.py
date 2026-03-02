import encoder

def test_encode_word():
    word = "hello"
    shift = 5

    assert encoder.caesar_shift(word, shift) == "mjqqt"

def test_encode_phrase():
    string = "Mi bomboclat I'm THE Caesar"
    shift = 10

    assert encoder.caesar_shift(string, shift) == "Ws lywlymvkd S'w DRO Mkockb"

def test_decode_word():
    encoded_word = "mjqqt"
    shift  = -5

    assert encoder.caesar_shift(encoded_word, shift) == "hello"

def test_decode_phrase():
    encoded_phrase = "Ws lywlymvkd S'w DRO Mkockb"
    shift = -10

    assert encoder.caesar_shift(encoded_phrase, shift) == "Mi bomboclat I'm THE Caesar"