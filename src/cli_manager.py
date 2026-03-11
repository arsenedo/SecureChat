class CLICommand:
    def __init__(self, aliases: list[str] = [], description: str = ""):
        self.aliases = "".join(f"/{alias}{", " if i < len(aliases) - 1 else ""}" for i, alias in enumerate(aliases))
        self.description = description

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

    commands = []
    def __init__(self):
        print(self.header)

    def add_command(self, command: CLICommand):
        self.commands.append(command)

    def print_available_commands(self):
        print(self.available_commands_header)
        
        for command in self.commands:
            print(command.aliases[0] + " \t-" + command.description)