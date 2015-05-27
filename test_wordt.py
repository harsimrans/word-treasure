import unittest
from word_treasure import *

class WordTreasureTestCase(unittest.TestCase):
    """Test for functions in word treasure.
    The major aim is to check if there is any
    unexpected crash.
    Doesnot check the validity of the response"""

    def test_definition_call(self):
        word1 = "hello"
        word2 = "somenonexistantword"
        display_definitions(word1)
        display_definitions(word2)
        return True

    def test_random_words(self):
        limit = 10
        display_random_words(limit)
        return True
    def test_display_examples(self):
        limit = 10
        word1 = "hello"
        word2 = "somenonexistantword"
        display_examples(word1, limit)
        display_examples(word2, limit)
        return True
    def test_display_top_examples(self):
        word1 = "hello"
        word2 = "somenonexistantword"
        display_top_examples(word1)
        display_top_examples(word2)
        return True
    def test_display_related_words(self):
        word1 = "hello"
        word2 = "somenonexistantword"
        display_related_words(word1)
        display_related_words(word2)
        return True
    def test_display_compact(self):
        word1 = "hello"
        word2 = "somenonexistantword"
        display_compact(word1)
        display_compact(word2)
        return True
    def test_help_display(self):
        display_help()
        return True

if __name__=='__main__':
    unittest.main()
