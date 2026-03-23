from payload import PayloadType

class CLICommand:
    def __init__(self, callback: function[str, str], aliases: list[str] = [], flags: list[str] = "", input_options: list[str] = ""):
        self.aliases = aliases
        self.input_options = input_options
        self.flags = flags
        self.callback = callback

    def execute(self, flag: str = None, user_input: str = None):
        self.callback(flag, user_input)
        
    def to_string(self):
        str_final = ""

        str_aliases = ", ".join(f"/{alias}" for alias in self.aliases)
        if str_aliases is not "":
            str_final += str_aliases

        str_flags = ", ".join(f"-{flag}" for flag in self.flags)
        if str_flags is not "":
            str_final += " " + str_flags

        str_user_input = "|".join(f"{input_option}" for input_option in self.input_options)
        if str_user_input is not "":
            str_user_input = "<" + str_user_input + ">"
            str_final += " " + str_user_input 

        return str_final
    
class ParsedCLICommand:
    def __init__(self, command: str, flag: PayloadType = None, user_input: str = None):
        self.command = command
        self.flag = flag
        self.user_input = user_input