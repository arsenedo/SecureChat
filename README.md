# Secure Chat App
Course project of 103.2 CrySec

# Objectives
* Design and implementation of a complete application with GUI and network communication
* Implementation of cryptographic methods
* Autonomous Development

# Constraints
* Python
* Initially CLI then GUI 
* Communication with a provided server

# Project Communication Protocol
Address: vlbelintrocrypto.hevs.ch
Port: 6000

## Overview
1. Transport Layer: TCP & Sockets
    * Communication happens over TCP, which ensures reliable and ordered message delivery as well as error-checks
    * Sockets are used, which are implemented using network programming APIs
2. Message format (General Structure):
    All messages follow a standard format that starts with a header
3. Connection rule
    * If the expected message structure is not followed, the connection is terminated

## Header
### Overview
![header image](/readme-static/header.png)
* **1st, 2nd and 3rd bytes** : Always the string 'ISC' (used as a protocol identifier)
* **4th byte** : Indicates the type of message, which can be:
    * 't' -> Text message
    * 's' -> Server-only message (not broadcasted)
    * 'i' -> Image message

### Message
* **Text / Server Messages** ('t' or 's')
    * 5th & 6th bytes: Store the number of characters in the message (N) as a big-endian 2-byte integer
    * N * 4 bytes: The actual message, where:
        * Each char is 4 bytes long (big-endian order)
        * The string is UTF-8 encoded
    * Server-only messages ('s'): These are meant only for server communication and are not broadcast to all users
* **Image messages** ('i')
    * 5th byte: Image width (max 128 pixels)
    * 6th byte: Image height (max 128 pixels)
    * Following bytes: The image's pixel data in RGB format
        * Pixels are stored row by row (y-axis first, then x-axis)
        * Each pixel consists of 3 consecutive bytes(RGB-RGB-RGB)


# Implementation Notes
## CLI user input
* The user input can have multiple fields and each field might contain multiple options.
* The fields might be optional

# Diagrams
## TCP Client and payload Building
```mermaid
---
config:
  class:
    hideEmptyMembersBox: true
---
classDiagram
direction TB
    class Client {
        + bytes_per_char: int
        + payload_builder: PayloadBuilder
	    + connect(IP_address: str, port: int)
	    + send(message: str, msg_type: PayloadType)
	    + receive(timeout: int) Payload
	    + close()
    }

    class PayloadBuilder {
	    + create(type: PayloadType, message: str) Payload
        + parse(payload: bytes) Payload
    }

    class Payload {
        + header: bytes
        + type: bytes
        + length: bytes
        + message: bytes
        + to_bytes() bytes

    }

    Client --> PayloadBuilder
```

## CLI MVC and Command Pattern
The command pattern is used because this app will have a CLI and a GUI. Both do the exact same thing so we need to centralize the logic inside of commands

The MVC pattern was simplified to a MV and a base handler which parses the command and passes the parsed information to the model. Which in turns executes the desired command
```mermaid
---
config:
  layout: dagre
  class:
    hideEmptyMembersBox: true
---
classDiagram
direction BT
    class Main {
    }

    class CommandInvoker {
	    - command: Command
	    + set_command(command: Command)
	    + execute_command()
    }

    class Command {
    }

    class CLIHandler {
        - cli_model: CLIModel
        + execute_cli_command(cli_command: str)
    }

    class CLIView {
	    + print_header()
	    + print_available_commands(cli_commands: list[CLICommand])
    }

    class CLIModel {
	    - cli_view: CLIView
	    - command_invoker: CommandInvoker
	    + CLIModel(command_invoker: CommandInvoker)
        + get_available_commands() list[CLICommand]
    }

    CLIHandler --> CLIModel
    Main --> CLIHandler
    Main --> CommandInvoker
    CLIModel --> CommandInvoker
    CLIModel --> CLIView
    CommandInvoker --> Command
```