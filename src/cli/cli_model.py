from cli.cli_view import CLIView
from cli.cli_command import *
from payload import PayloadType
from commands.command_invoker import CommandInvoker, ICommand
from commands.send_text_command import *
from commands.select_message_to_buffer import *
from commands.set_message_to_buffer import *
from commands.show_current_buffers import *
from commands.caesar_shift_command import *
import os


class CLIModel:
    def __init__(self, view: CLIView, command_invoker: CommandInvoker):
        self.cli_view = view
        self.command_invoker = command_invoker
        
        view.print_header()

    def execute_parsed_command(self, parsed_command: ParsedCLICommand):
        command = next((cli_command for cli_command in self.get_cli_commands() if parsed_command.command in cli_command.aliases), None)

        if not command:
            self.cli_view.print_string(f"Command {parsed_command.command} not found")
            return

        command.execute(parsed_command.flag, parsed_command.user_input)

    def get_cli_commands(self):          
        return [
            CLICommand(
                aliases = ["help"], 
                callback = lambda flag, user_input : self.cli_view.print_available_commands(self.get_cli_commands())
            ),
            CLICommand(
                aliases = ["quit", "exit", "q"], 
                callback = lambda flag, user_input : os._exit(0)
            ),
            CLICommand(
                aliases = ["send"],
                input_options = [InputOptionsList(["text", "plain", "encoded"])],
                flags = ["s"],
                callback = lambda flag, user_input : self.set_and_execute_invoker(SendTextCommand(user_input, flag))
            ),
            CLICommand(
                aliases = ["select"],
                input_options = [InputOptionsList(["i"]), InputOptionsList(["e", "c"], True)],
                callback = lambda flag, user_input : self.set_and_execute_invoker(SelectMessageToBuffer(user_input))
            ),
            CLICommand(
                aliases = ["set"],
                input_options = [InputOptionsList(["plain", "encoded"]), InputOptionsList(["text"])],
                callback = lambda flag, user_input : self.set_and_execute_invoker(SetMessageToBuffer(user_input))
            ),
            CLICommand(
                aliases = ["show"],
                input_options = [InputOptionsList(["stringify"])],
                callback = lambda flag, user_input : self.set_and_execute_invoker(ShowCurrentBuffers(self.cli_view, user_input))
            ),
            CLICommand(
                aliases = ["encode"],
                input_options = [InputOptionsList(["shift"]), InputOptionsList(["k"])],
                callback = lambda flag, user_input : self.set_and_execute_invoker(CaesarShiftCommand(user_input, True))
            ),
            CLICommand(
                aliases = ["decode"],
                input_options = [InputOptionsList(["shift"]), InputOptionsList(["k"])],
                callback = lambda flag, user_input : self.set_and_execute_invoker(CaesarShiftCommand(user_input, False))
            )
        ]
    
    def set_and_execute_invoker(self, command: ICommand):
        self.command_invoker.set_command(command)
        self.command_invoker.execute_command()
