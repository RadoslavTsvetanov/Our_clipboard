from parser import Parser
import sys
sys.path.insert(0,"./clipboard_interacter")
from clipboard_interacter.clipboard import ClipboardMonitor
from clipboard_interacter.client import SocketClient


class CLI:
    def __init__(self) -> None:
        pass

    def start_session(self, name):
        base_url = "ws://localhost:8080"
        socket_client = SocketClient(
            name, base_url, ClipboardMonitor(base_url).change_clipboard)
        clipboard_monitor = ClipboardMonitor(socket_client)

        socket_client.start()  # ! establishes both the listener and the sender
        clipboard_monitor.monitor_clipboard(interval_seconds=1)
        print("start_session")

    def end_session(self, name):
        print("ending session")

    def send_manually(self, message):
        print("sending manually")


cli = CLI()
parser = Parser(sys.argv)
if (parser.check_for_option("--start")):
    cli.start_session(parser.get_option_value("--name"))
elif (parser.check_for_option("--end")):
    cli.end_session(parser.get_option_value("--name"))
elif (parser.check_for_option("--send")):
    cli.send_manually(parser.get_option_value("--message"))
