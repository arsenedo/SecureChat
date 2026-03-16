class CLICommand:
    def __init__(self, callback: function, aliases: list[str] = []):
        self.aliases = aliases
        self.callback = callback

    def execute(self):
        self.callback()
        
    def to_string(self):
        str_aliases = ", ".join(f"/{alias}" for alias in self.aliases)

        return str_aliases