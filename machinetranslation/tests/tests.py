#recognized_text = "hello, nice to meet you"
import unittest

from translator import *

class english_to_french_unittests(unittest.TestCase): 
    def test1(self): 
    	"""unit test function"""
    	self.assertEqual(english_to_french("hello").lower(), "bonjour")
    	self.assertEqual(english_to_french(""), "")
    	self.assertEqual(english_to_french("welcome").lower(), "bienvenue")


class english_to_german_unittests(unittest.TestCase): 
    def test2(self): 
    	"""unit test function"""
    	self.assertEqual(english_to_german("hello").lower(), "hallo")
    	self.assertEqual(english_to_german(""), "")
    	self.assertEqual(english_to_german("love").lower(), "liebe")

unittest.main()
