from pynput.keyboard import Key, Listener

# Complete mappings referenced from your keycodes.txt
SPECIAL_KEYS = {
    Key.space: " ",
    Key.enter: "\n",
    Key.backspace: "[BACKSPACE]",
    Key.tab: "[TAB]",
    Key.caps_lock: "[CAPS_LOCK]",
    Key.shift: "",
    Key.shift_r: "",
    Key.ctrl_l: "",
    Key.ctrl_r: "",
    Key.alt: "",
    Key.alt_r: "",
}

def start_keyboard_listener(callback_function):
    """
    Spawns the OS-level global keyboard input hook thread.
    Passes extracted characters into the provided callback function.
    """
    def internal_on_press(key):
        try:
            # Handle standard letters and numbers safely
            letter = key.char if key.char is not None else ""
        except AttributeError:
            # Fallback to mapped special keys or a raw fallback name
            letter = SPECIAL_KEYS.get(key, f"[{key.name.upper()}]")
        
        # Pass the processed string out to the callback
        callback_function(letter)

    # Context manager setup for OS input stream interception
    return Listener(on_press=internal_on_press)