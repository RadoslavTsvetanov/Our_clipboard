import time
import pyperclip
# from client import SocketClient


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

            message = {"data": current_clipboard_data}
            self.web_socket_client.send_data(message)

    def monitor_clipboard(self, interval_seconds):
        while True:
            self.check_clipboard_change()
            time.sleep(interval_seconds)

    def listen_socket(self):
        self.web_socket_client.listen_thread.start()

    def change_clipboard(self, message):
        print(f"copying {message} to clipboard")
        pyperclip.copy(message)


# # Example usage
# if True:
#     socket_id = "example_socket"
#     # Adjust the base_url accordingly
#     base_url = "ws://k63mgfkn-8080.euw.devtunnels.ms/"

#     socket_client = SocketClient(
#         socket_id, base_url, ClipboardMonitor(base_url).change_clipboard)
#     clipboard_monitor = ClipboardMonitor(socket_client)

#     socket_client.start()  # ! establishes both the listener and the sender
#     clipboard_monitor.monitor_clipboard(interval_seconds=1)
