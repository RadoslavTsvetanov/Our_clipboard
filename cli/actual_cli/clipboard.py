import pyperclip
import threading
import time

def get_clipboard():
    return pyperclip.paste()

class Clipboard:
    def __init__(self):
        self.clipboard = get_clipboard()


    def set_clipboard(self,text)->None:
       self.clipboard = text 

    def get_clipboard(self):
        return self.clipboard

    def listen_for_change(self,callback):
        while True:
            if self.get_clipboard() !=  get_clipboard():
                self.set_clipboard(get_clipboard()) 
                if callback is not None:
                    callback(self.get_clipboard) #this will call the socket.send_message
            time.sleep(1)
            