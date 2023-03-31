import unittest
from translator import englishToFrench, frenchToEnglish

class TestSquare(unittest.TestCase): 
    def test_english(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test for the translation of the world ‘Hello’ and ‘Bonjour’.
        self.assertEqual(englishToFrench(''), '')  # test for null input.
        
class TestDouble(unittest.TestCase): 
    def test_french(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test for the translation of the world ‘Bonjour’ and ‘Hello’.
        self.assertEqual(frenchToEnglish(''), '') # test for null input.
        

unittest.main()