import unittest
import sys
import os

# Appends the src directory to the system path so tests can run easily
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from core.buffer import KeyBuffer

class TestKeyBuffer(unittest.TestCase):
    
    def test_buffer_addition(self):
        """Verifies characters are safely held in volatile memory."""
        kb = KeyBuffer(max_size=5)
        kb.add("a")
        kb.add("b")
        self.assertFalse(kb.is_full())

    def test_buffer_overflow_trigger(self):
        """Verifies that the buffer correctly flags when it hits its capacity threshold."""
        kb = KeyBuffer(max_size=3)
        kb.add("x")
        kb.add("y")
        kb.add("z")
        self.assertTrue(kb.is_full())

    def test_buffer_flush(self):
        """Ensures clearing the cache consolidates the data cleanly and resets it."""
        kb = KeyBuffer(max_size=3)
        kb.add("1")
        kb.add("2")
        
        data_chunk = kb.flush()
        self.assertEqual(data_chunk, "12")
        self.assertEqual(len(kb.buffer), 0)

if __name__ == '__main__':
    unittest.main()