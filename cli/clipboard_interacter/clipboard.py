import time
import pyperclip
from socket_client.Client import *


class ClipboardMonitor:
    def __init__(self, web_socket_client):
        self.previous_clipboard_data = pyperclip.paste()
        self.web_socket_client = web_socket_client

    def check_clipboard_change(self):
        current_clipboard_data = pyperclip.paste()
        if current_clipboard_data != self.previous_clipboard_data:
            print("Clipboard change detected: {}".format(
                current_clipboard_data))
            self.previous_clipboard_data = current_clipboard_data

            # Send the changed clipboard data to the WebSocket server
            message = {"clipboard_data": current_clipboard_data}
            self.web_socket_client.send_message(json.dumps(message))

    def monitor_clipboard(self, interval_seconds):
        while True:
            self.check_clipboard_change()
            time.sleep(interval_seconds)

    def listen_socket(self):
        self.web_socket_client.li


socket = WebSocketClient("http://localhost:3000/")
clipboard_monitor = ClipboardMonitor()
clipboard_monitor.monitor_clipboard(interval_seconds=1)
