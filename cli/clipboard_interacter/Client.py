import websocket
import json
import threading


class SocketClient:
    def __init__(self, socket_id, baseurl, on_message_callback):
        self.socket_id = socket_id
        self.socket_url = f"{baseurl}/socket/{socket_id}"
        self.ws = websocket.WebSocketApp(
            self.socket_url, on_message=self.on_message)
        self.send_thread = threading.Thread(target=self.send_messages)
        self.listen_thread = threading.Thread(target=self.listen)
        self.running = True
        self.on_message_callback = on_message_callback

    def on_message(self, ws, message):
        data = json.loads(message)
        print(f"Received message from {data['id']}: {data['data']}")
        if self.on_message_callback:
            self.on_message_callback(data['data'])

    def listen(self):
        print("hi")
        while self.running:
            self.ws.run_forever()

    def send_data(self, data):
        message = {"id": self.socket_id, "data": data}
        self.ws.send(json.dumps(message))

    def send_messages(self):
        while self.running:
            message = input("Enter message to send (type 'exit' to quit): ")
            if message.lower() == "exit":
                self.running = False
                break
            self.send_data(message)

    def start(self):
        self.send_thread.start()
        self.listen_thread.start()

    def join(self):
        self.send_thread.join()
        self.listen_thread.join()

    def close(self):
        self.running = False
        self.ws.close()


# Example usage
if __name__ == "__main__":
    socket_id = "example_socket"
    base_url = "ws://localhost:8080"  # Adjust the base_url accordingly
    client = SocketClient(socket_id, base_url, None)
    client.start()
    client.join()
