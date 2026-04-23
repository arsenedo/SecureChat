import encoder, pytest

@pytest.mark.parametrize(
        "string, key, expected",
        [
            (
                "hello",
                "world",
                "ßÔÞØÓ"
            ),
            (
                "Stellar Velocity 🚀",
                "Quantum",
                "¤éÆÚàÖßqËÆÚãØÖÅî🛮"
            )
        ]
)
def test_vigenere_encode(string, key, expected):
    encoded_string = encoder.vigenere_encode(string.encode("utf-32-be"), key.encode("utf-32-be"))

    assert(encoded_string == expected.encode("utf-32-be"))


@pytest.mark.parametrize(
        "string, key, expected",
        [
            (
                "ßÔÞØÓ",
                "world",
                "hello"
            ),
            (
                "¤éÆÚàÖßqËÆÚãØÖÅî🛮",
                "Quantum",
                "Stellar Velocity 🚀",
            )
        ]
)
def test_vigenere_decode(string, key, expected):
    decoded_string = encoder.vigenere_decode(string.encode("utf-32-be"), key.encode("utf-32-be"))

    assert(decoded_string == expected.encode("utf-32-be"))