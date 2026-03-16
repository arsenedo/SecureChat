from encoder import caesar_shift
import pytest

# TODO CHANGE TEXT
@pytest.mark.parametrize(
    "message, n, expected",
    [
        (
            "Hello, World!",
            10,
            "Rovvy6*ay|vn+",
        ),
        (
            "ꯂ Perspectives critiques 믂, 5 f꧃vrier 2020",
            10,
            "ꯌ*Zo|}zom~s\u0080o}*m|s~s{\u007fo}*믌6*?*p꧍\u0080|so|*<:<:",
        ),
    ],
)
def test_encrypt(message: str, n: int, expected: str):
    result = caesar_shift(message, n)

    assert result == expected

@pytest.mark.parametrize(
    "message, n, expected",
    [
        (
            "Rovvy6*ay|vn+",
            10,
            "Hello, World!",
        ),
        (
            "ꯌ*Zo|}zom~s\u0080o}*m|s~s{\u007fo}*믌6*?*p꧍\u0080|so|*<:<:",
            10,
            "ꯂ Perspectives critiques 믂, 5 f꧃vrier 2020",
        ),
    ],
)
def test_decrypt(message: str, n: int, expected: str):
    result = caesar_shift(message, -n)

    assert result == expected