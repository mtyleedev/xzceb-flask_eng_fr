import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertIsNone(englishToFrench(''))
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertIsNone(frenchToEnglish(''))
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
