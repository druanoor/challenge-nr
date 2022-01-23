import unittest
import sys

from app import readInput, clearInput, fillStringDictionary

class TestSum(unittest.TestCase):
    def test_readInput(self):
        """
        Test that input is properly read
        """
        
        result = len(readInput(sys.argv))
        self.assertGreater(result, 0)
    
    def test_clearInput(self):
        """
        Test that input is properly read
        """
        inputString = "---!!a`+[a"
        result = clearInput(inputString)
        self.assertNotIn("-", result)

    def test_fillStringDictionary(self):
        """
        Test that input is properly read
        """
        inputString = "one two three four five"
        dictionary = {}
        result = fillStringDictionary(dictionary, inputString)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main(argv=['text-examples/moby-dick.txt'])