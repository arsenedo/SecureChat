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
        for command in commands:
            print(command.to_string())

    def print_string(self, string: str):
        print(string)