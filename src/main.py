import client

IP_address = "vlbelintrocrypto.hevs.ch"
port = 6000

def main():
    c = client.Client()

    c.connect(IP_address, port)

    c.send("bruh")

    payload = c.receive(1)

    print(payload.message.decode("utf-32-be"))


if __name__ == "__main__":
    main()
