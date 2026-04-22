from encoder import rsa_encode
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