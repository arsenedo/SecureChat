import client
from payload import PayloadType
from encoder import Encoder
from threading import Thread
from cli import cli_handler
from commands.command_invoker import CommandInvoker


IP_address = "vlbelintrocrypto.hevs.ch"
port = 6000

def listen_to_server(c: client.Client, cli: cli_handler.CLIHandler):
    while True:
        payload = c.receive()
        
        last_msg: tuple[int, bytes] = c.get_last_message()
        cli.model.cli_view.print_string(f"{last_msg[0]}: {last_msg[1].decode("utf-8", "replace")}")

def main():
    c = client.Client()

    encoder = Encoder()

    command_invoker = CommandInvoker(c, encoder)

    cli = cli_handler.CLIHandler(command_invoker)

    print(f"[+] Connecting to {IP_address}:{port}")
    c.connect(IP_address, port)
    print(f"[+] Connected successfully")
    print(f"Connected to {IP_address}:{port}")

    thread = Thread(target = listen_to_server, kwargs = {"c": c, "cli": cli})

    thread.start()

    cli.execute_cli_command("/help")

    while True:
        user_input: str = input()
        cli.execute_cli_command(user_input)
        #c.send(user_input, PayloadType.TEXT)

if __name__ == "__main__":
    main()
