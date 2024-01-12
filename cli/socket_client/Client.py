import threading
import requests
import websocket
import json


class WebSocketClient:
    def __init__(self, url):
        self.url = url
        self.ws = None
        self.ws_lock = threading.Lock()

    def establish_connection(self):
        with self.ws_lock:
            if self.ws is None:
                self.ws = websocket.create_connection(self.url)
                print(f"WebSocket connection established: {self.url}")

    def close_connection(self):
        with self.ws_lock:
            if self.ws is not None:
                self.ws.close()
                self.ws = None
                print("WebSocket connection closed.")

    def join_socket(self):
        try:
            self.establish_connection()
            while True:
                message = self.ws.recv()
                self.handle_message(message)
        except Exception as e:
            print(f"Failed to connect to WebSocket. Error: {e}")
        finally:
            self.close_connection()

    def send_message(self, message):
        try:
            self.establish_connection()
            self.ws.send(message)
            print(f"Sent message: {message}")
        except Exception as e:
            print(f"Failed to send message. Error: {e}")
        finally:
            self.close_connection()

    def listen_for_messages(self):
        try:
            self.establish_connection()
            while True:
                message = self.ws.recv()
                self.handle_message(message)
        except Exception as e:
            print(f"Failed to listen for messages. Error: {e}")
        finally:
            self.close_connection()

    def handle_message(self, message):
        print(f"Received message from WebSocket: {message}")
