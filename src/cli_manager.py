class CommandArg:
    def __init__(self, value: str, is_optional = False):
        self.value = value
        self.is_optional = is_optional

class CLICommand:
    """
    aliases - what can be called
    description - short description of the command
    user_input - text, which the user can pass to the command. Appears between <>
    """
    def __init__(self, aliases: list[str] = [], description: str = "", user_input: str = "", args: list[CommandArg] = []):
        self.aliases = aliases
        self.user_input = user_input
        self.description = description
        self.args = args

    def to_string(self):
        formatted_aliases = ", ".join(f"/{alias}" for alias in self.aliases)
        formatted_user_input = f"<{self.user_input}>" if self.user_input != "" else ""
        formatted_description = f"\t- {self.description}"

        formatted_args = " ".join(f"-{arg.value}" for arg in self.args)

        final_string = ""

        if formatted_aliases != "":
            final_string += formatted_aliases + " "
        
        if formatted_args != "":
            final_string += formatted_args + " "
        return final_string + formatted_user_input + formatted_description

class CLIManager:
    header = """
======================================================
\tCryptoSecuritySocialNetwork - CLI
======================================================
"""

    available_commands_header = """
======================================================
\tAVAILABLE COMMANDS
======================================================
"""

    def __init__(self):
        print(self.header)

    def add_command(self, command: CLICommand):
        self.commands.append(command)

    def print_available_commands(self):
        print(self.available_commands_header)
        
        for command in self.get_commands():
            print(command.to_string())

    def get_commands(self):
        return [
            CLICommand(
                aliases = ["help"],
                description = "Show this message"
            ),
            CLICommand(
                aliases = ["quit", "exit", "q"],
                description = "Disconnect and exit"
            ),
            CLICommand(
                aliases = ["send"],
                user_input = "text",
                description = "Send to all clients"
            ),
            CLICommand(
                aliases = ["send"],
                user_input = "text",
                args = [
                    CommandArg(
                        "s",
                    )
                ],
                description = "Send to server"
            ),
            CLICommand(
                user_input="text",
                description = "Send to all clients"
            )
        ]