from encoder import rsa_encode, rsa_decode
import pytest

@pytest.mark.parametrize(
    "message, n, e, expected_int",
    [
        (b"f", 3233, 17, 1369),
        (b"\x02", 21, 5, 11),
    ],
)
def test_rsa_encrypt_parametrized(message, n, e, expected_int):
    result_bytes = rsa_encode(message, n, e)
    result_int = int.from_bytes(result_bytes, 'big')

@pytest.mark.parametrize(
    "message, n, d, expected_string",
    [
        ("141 95 137 112 128 111 199 95 230 79", 259, 173, "cryptogram"),
    ],
)
def test_rsa_decrypt(message, n, d, expected_string):
    results_bytes = rsa_decode(message.encode("utf-32-be"), n, d)

    results_bytes.decode("utf-32-be") == expected_string
