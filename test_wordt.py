import unittest
from word_treasure import *

class WordTreasureTestCase(unittest.TestCase):
    """Test for word treasure."""
    def test_definition_call(self):
        word = "hello"
        display_definitions(word)
        return True

if __name__=='__main__':
    unittest.main()
