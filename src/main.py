import client
from payload import PayloadType
from encoder import Encoder
from threading import Thread
from cli import cli_handler
from commands.command_invoker import CommandInvoker
from gui import MainWindow
import os, sys
from PyQt6.QtWidgets import QApplication


IP_address = "vlbelintrocrypto.hevs.ch"
port = 6000

def listen_to_server(c: client.Client, cli: cli_handler.CLIHandler, gui: MainWindow):
    while True:
        payload = c.receive()
        
        last_msg: tuple[int, bytes] = c.get_last_message()
        str_msg: str = f"{last_msg[0]}: {last_msg[1].decode("utf-32-be", "replace")}"
        cli.model.cli_view.print_string(str_msg)
        gui.appendToMessageDisplay(str_msg)


def handle_cli(cli: cli_handler.CLIHandler):
    cli.execute_cli_command("/help")

    while True:
        user_input: str = input()
        cli.execute_cli_command(user_input)

def main():
    c = client.Client()
    encoder = Encoder()

    command_invoker = CommandInvoker(c, encoder)

    app = QApplication(sys.argv)
    gui = MainWindow(command_invoker, encoder)
    

    cli = cli_handler.CLIHandler(command_invoker)
    cli.model.cli_view.print_string(f"[+] Connecting to {IP_address}:{port}")
    c.connect(IP_address, port)
    cli.model.cli_view.print_string(f"[+] Connected successfully")
    cli.model.cli_view.print_string(f"Connected to {IP_address}:{port}")

    listener_thread = Thread(target = listen_to_server, kwargs = {"c": c, "cli": cli, "gui": gui})

    listener_thread.start()

    cli_thread = Thread(target = handle_cli, kwargs = {"cli": cli})

    cli_thread.start()

    os._exit(app.exec())

if __name__ == "__main__":
    main()
