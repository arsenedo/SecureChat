import pytest
import utils.cli_utils as cli_utils
from cli.cli_command import ParsedCLICommand

@pytest.mark.parametrize(
        "command, expected",
        [
            (
                "/help",
                ["help", None, None]
            ),
            (
                "/help -r",
                ["help", "r", None]
            ),
            (
                "/help -r I dont understand anything bro!!! T_T",
                ["help", "r", "I dont understand anything bro!!! T_T"]
            ),
            (
                "What a beautiful text i'm sending!",
                ["send", None, "What a beautiful text i'm sending!"]
            )
        ]
)
def test_command(command: str, expected: tuple[str, str, str]):
    parsed_command: ParsedCLICommand = cli_utils.parse_cli_command(command)

    print(parsed_command.command)
    assert parsed_command.command == expected[0]
    assert parsed_command.flag == expected[1]
    assert parsed_command.user_input == expected[2]