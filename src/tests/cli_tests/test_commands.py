import pytest
import utils.cli_utils as cli_utils
from cli.cli_command import ParsedCLICommand
from payload import PayloadType

@pytest.mark.parametrize(
        "command, expected",
        [
            (
                "/help",
                ["help", PayloadType.TEXT, None, None]
            ),
            (
                "/help -s",
                ["help", PayloadType.SERVER_TEXT, None, None]
            ),
            (
                "/help -s I dont understand anything bro!!! T_T",
                ["help", PayloadType.SERVER_TEXT, "I dont understand anything bro!!! T_T", None]
            ),
            (
                "What a beautiful text i'm sending!",
                ["send", PayloadType.TEXT, "What a beautiful text i'm sending!", None]
            ),
            (
                "/encode shift 5",
                ["encode", PayloadType.TEXT, "5", "shift"]
            ),
            (
                "/decode vigenere awdugjwJada[as]aw",
                ["decode", PayloadType.TEXT, "awdugjwJada[as]aw", "vigenere"]
            ),
            (
                "/encode rsa hgrhdg48757835 15",
                ["encode", PayloadType.TEXT, "hgrhdg48757835 15", "rsa"]
            )
        ]
)
def test_command(command: str, expected: tuple[str, str, str]):
    parsed_command: ParsedCLICommand = cli_utils.parse_cli_command(command)

    assert parsed_command.command == expected[0]
    assert parsed_command.flag == expected[1]
    assert parsed_command.user_input == expected[2]
    assert parsed_command.sub_type == expected[3]