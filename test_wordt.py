import unittest
from word_treasure import *

class WordTreasureTestCase(unittest.TestCase):
    """Test for word treasure."""
    def test_definition_call(self):
        word = "hello"
        display_definitions(word)
        return True

    def test_random_words(self):
        limit = 10
        display_random_words(limit)
        return True
    def test_display_examples(self):
        limit = 10
        word = "hello"
        display_examples(word, limit)
        return True
    def test_display_top_examples(self):
        word = "hello"
        display_top_examples(word)
        return True
    def test_display_related_words(self):
        word = "hello"
        display_related_words(word)
        return True
    def test_display_compact(self):
        word = "hello"
        display_compact(word)
        return True
    def test_help_display(self):
        display_help()
        return True

if __name__=='__main__':
    unittest.main()
