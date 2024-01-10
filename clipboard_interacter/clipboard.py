import pyperclip
from pynput import keyboard as keyboard_listener


class Clipboard:
    def __init__(self):
        self.current_clipboard_state = ""
        self.listener = None

    def get_clipboard_state(self):
        return pyperclip.paste()

    def set_clipboard_state(self, state):
        pyperclip.copy(state)

    def are_keys_pressed(self, keys):
        current_keys = set(keys)
        return current_keys.issubset(self.current_keys)

    def on_press(self, key):
        try:
            current_key = key.char
        except AttributeError:
            current_key = str(key)

        self.current_keys.add(current_key)

        if self.are_keys_pressed(['ctrl', 'c']):
            self.send_request()

    def on_release(self, key):
        try:
            current_key = key.char
        except AttributeError:
            current_key = str(key)

        self.current_keys.discard(current_key)

    def set_event_listener(self):
        with keyboard_listener.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            self.listener = listener
            listener.join()

    def send_request(self):
        clipboard_content = self.get_clipboard_state()
        print("Clipboard content:", clipboard_content)
        # Add your logic to send a request or perform any other action based on the clipboard content


# Example Usage:
clipboard_instance = Clipboard()
clipboard_instance.set_event_listener()
