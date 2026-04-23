from encoder import difhel_secret
import pytest

@pytest.mark.parametrize(
    "n, my_private, partner_public, secret",
    [
        (
            23,
            6,
            19,
            2
        ),
        (
            29,
            5,
            7,
            16
        )
    ],
)
def test_dif_hel(n: int, my_private: int, partner_public: int, secret: int):
    assert difhel_secret(n, my_private, partner_public) == secret