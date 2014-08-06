import unittest
from lab3 import *

class Lab(unittest.TestCase):
  def setup(self):
    pass

  def test_shout(self):
    self.assertEqual("I HATE DAVE.", shout("I hate Dave."))
	
  def test_reverse(self):
    self.assertEqual("916", reverse("619"))
	
  def test_reversewords(self):
    self.assertEqual("I hate Dino.", reversewords("Dino hate I."))
	
  def test_reversewordletters(self):
    self.assertEqual("noohgnuyM setah flesmih.", reversewordletters("Myunghoon hates himself."))
	
  def test_piglatin(self):
    self.assertEqual("unhappyway", piglatin("unhappy"))
	
if __name__ == '__main__':
  unittest.main()
  
