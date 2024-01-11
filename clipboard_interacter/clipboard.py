import time
import pyperclip


class ClipboardMonitor:
    def __init__(self):
        self.previous_clipboard_data = pyperclip.paste()

    def check_clipboard_change(self):
        current_clipboard_data = pyperclip.paste()
        if current_clipboard_data != self.previous_clipboard_data:
            print("Clipboard change detected: {}".format(current_clipboard_data))
            self.previous_clipboard_data = current_clipboard_data

    def monitor_clipboard(self, interval_seconds):
        while True:
            self.check_clipboard_change()
            time.sleep(interval_seconds)


clipboard_monitor = ClipboardMonitor()
clipboard_monitor.monitor_clipboard(interval_seconds=1)
