from cli.cli_command import *

class CLIView:
    def print_header(self):
        header = """
===================================================
\tCryptoSecuritySocialNetwork - CLI
===================================================
"""
        print(header)

    def print_available_commands(self, commands: CLICommand):
        title = """
===================================================
\tAVAILABLE COMMANDS
==================================================="""

        footer = """===================================================
"""

        print(title)
        for command in commands:
            print(f"{command.to_string()}")
        print(footer)

    def print_string(self, string: str):
        print(string)