import client
from payload import PayloadType

IP_address = "vlbelintrocrypto.hevs.ch"
port = 6000

def main():
    c = client.Client()

    c.connect(IP_address, port)

    c.send("pipi", PayloadType.TEXT)

    payload = c.receive()

    print(payload.message.decode("utf-8"))

    c.close()

if __name__ == "__main__":
    main()
