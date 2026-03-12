class CLICommand:
    def __init__(self, aliases: list[str] = []):
        self.aliases = aliases
        
    def to_string(self):
        str_aliases = ", ".join(f"/{alias}" for alias in self.aliases)

        return str_aliases