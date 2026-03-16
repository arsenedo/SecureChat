class CLICommand:
    def __init__(self, callback: function, aliases: list[str] = []):
        self.aliases = aliases
        self.callback = callback

    def execute(self, msg):
        self.callback(msg)
        
    def to_string(self):
        str_aliases = ", ".join(f"/{alias}" for alias in self.aliases)

        return str_aliases
    
class ParsedCLICommand:
    def __init__(self, command: str, flag: str = None, user_input: str = None):
        self.command = command
        self.flag = flag
        self.user_input = user_input