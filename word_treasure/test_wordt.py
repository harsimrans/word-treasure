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
        self.assertEqual(display_definitions(word1), True)
        self.assertEqual(display_definitions(word2), None)
        
    def test_random_words(self):
        limit = 10
        self.assertEqual(display_random_words(limit), True)

    def test_display_examples(self):
        limit = 10
        word1 = "hello"
        word2 = "somenonexistantword"
        self.assertEqual(display_examples(word1, limit), True)
        self.assertEqual(display_examples(word2, limit), None)
        
    def test_display_top_examples(self):
        word1 = "hello"
        word2 = "somenonexistantword"
        self.assertEqual(display_top_examples(word1), True)
        self.assertEqual(display_top_examples(word2), None)
    
    def test_display_related_words(self):
        word1 = "hello"
        word2 = "somenonexistantword"
        self.assertEqual(display_related_words(word1), True)
        self.assertEqual(display_related_words(word2), None)
    
    def test_display_compact(self):
        word1 = "hello"
        word2 = "somenonexistantword"
        self.assertEqual(display_compact(word1), True)
        self.assertEqual(display_compact(word2), None)
    
    def test_help_display(self):
        self.assertEqual(display_help(), True)
    
if __name__=='__main__':
    unittest.main()
