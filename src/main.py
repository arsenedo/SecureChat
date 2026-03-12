import client
from payload import PayloadType
from threading import Thread
from cli import cli_handler


IP_address = "vlbelintrocrypto.hevs.ch"
port = 6000

def listen_to_server(c: client.Client):
    while True:
        payload = c.receive()
        print(payload.message.decode("utf-8"))

def main():
    c = client.Client()

    cli = cli_handler.CLIHandler()

    print(f"[+] Connecting to {IP_address}:{port}")
    c.connect(IP_address, port)
    print(f"[+] Connected successfully")
    print(f"Connected to {IP_address}:{port}")

    thread = Thread(target = listen_to_server, kwargs = {"c": c})

    thread.start()

    return
    while True:
        user_input: str = input()
        c.send(user_input, PayloadType.TEXT)

if __name__ == "__main__":
    main()
