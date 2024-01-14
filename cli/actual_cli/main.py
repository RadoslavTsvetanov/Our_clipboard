from Parser import Parser
import sys
sys.path.insert(0,"./clipboard_interacter")
from clipboard import Clipboard
from client import SocketClient


class CLI:
    def __init__(self) -> None:
        pass

    def start_session(self, name):
        def handle_received_message(message):
        # Add your logic for handling received messages here
            print(f"Handling received message: {message}")

        socket_id = input("Enter socket ID: ")
        server_url = "localhost:8080"  # Replace with your server's URL
        client = SocketClient(socket_id, server_url, Clipboard(),
                          on_message_callback=True)
        client.run()


    def end_session(self, name):
        print("ending session")

    def send_manually(self, message):
        print("sending manually")


cli = CLI()
parser = Parser(sys.argv)
if (parser.check_for_option("--start")):
    cli.start_session()
elif (parser.check_for_option("--end")):
    cli.end_session(parser.get_option_value("--name"))
elif (parser.check_for_option("--send")):
    cli.send_manually(parser.get_option_value("--message"))
