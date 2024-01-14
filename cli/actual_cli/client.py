import websocket
import threading
from clipboard import Clipboard

class SocketClient:
    def __init__(self, socket_id, server_url,clipboard:Clipboard, on_message_callback=None):
        self.socket_id = socket_id
        self.server_url = server_url
        self.socket_url = f"ws://{server_url}/socket/{socket_id}"
        self.ws = websocket.WebSocketApp(self.socket_url,
                                         on_message=self._on_message,
                                         on_error=self._on_error,
                                         on_close=self._on_close)

        self.on_message_callback = on_message_callback
        self.clipboard = clipboard
        self.send_thread = threading.Thread(
            target=self.listen_for_clipboard_change, daemon=True)
        self.send_thread.start()

    def _on_message(self, ws, message):
        print(f"Received message: {message}")
        if self.on_message_callback:
            self.clipboard.set_clipboard(message)

    def _on_error(self, ws, error):
        print(f"Error: {error}")

    def _on_close(self, ws, close_status_code, close_msg):
        print("Connection closed")
    def send_message(self,message):
        self.ws.send(message)
    # def _start_send_thread(self):
    #     while True:
    #         message = input("Enter message to send: ")
    #         print(f"Sent message: {message}")
    #         self.send_message(message)

    def run(self):
        self.ws.run_forever()

    def listen_for_clipboard_change(self):
        self.clipboard.listen_for_change(lambda text: self.send_message(self.clipboard.get_clipboard()))


if __name__ == "__main__":
    def handle_received_message(message):
        # Add your logic for handling received messages here
        print(f"Handling received message: {message}")

    socket_id = input("Enter socket ID: ")
    server_url = "localhost:8080"  # Replace with your server's URL
    client = SocketClient(socket_id, server_url, Clipboard(),
                          on_message_callback=True)
    client.run()
