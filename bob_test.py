import unittest
from bob import *

class BOB(unittest.TestCase):
  def setup(self):
    pass
	
  def test_question(self):
    self.assertEqual("Sure.", bob("Are you cheating on me?"))
	 
  def test_yell(self):
    self.assertEqual("Woah, chill out!", bob("I CAN'T BELIEVE YOU WOULD DO THIS TO ME!"))
	
  def test_nothing(self):
    self.assertEqual("Fine. Be that way!", bob(""))
	
  def test_anything(self):
    self.assertEqual("Whatever.", bob("It's over between us!"))
	
if __name__ == '__main__':
  unittest.main()