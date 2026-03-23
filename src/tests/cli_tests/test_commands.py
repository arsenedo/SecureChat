import pytest
import utils.cli_utils as cli_utils
from cli.cli_command import ParsedCLICommand
from payload import PayloadType

@pytest.mark.parametrize(
        "command, expected",
        [
            (
                "/help",
                ["help", None, None]
            ),
            (
                "/help -s",
                ["help", PayloadType.SERVER_TEXT, None]
            ),
            (
                "/help -s I dont understand anything bro!!! T_T",
                ["help", PayloadType.SERVER_TEXT, "I dont understand anything bro!!! T_T"]
            ),
            (
                "What a beautiful text i'm sending!",
                ["send", PayloadType.TEXT, "What a beautiful text i'm sending!"]
            )
        ]
)
def test_command(command: str, expected: tuple[str, str, str]):
    parsed_command: ParsedCLICommand = cli_utils.parse_cli_command(command)

    print(parsed_command.command)
    assert parsed_command.command == expected[0]
    assert parsed_command.flag == expected[1]
    assert parsed_command.user_input == expected[2]