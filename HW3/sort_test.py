import unittest
from sort import *

class SortTest(unittest.TestCase):
  def setUp(self):
    self.test1 = [34,23,123,46534,543,45376,345,43,42,56,76,8,9,10]
    self.test2 = ['j', 'v', 'r', 's', 1, 5, 4]
    self.sorted1 = [8,9,10,23,34,42,43,56,76,123,345,543,45376,46534]
    self.sorted2 = [1, 4, 5, 'j', 'r', 's', 'v']

  def test_mergeSort(self):
    self.assertEqual(mergesort(self.test1), self.sorted1)
    self.assertEqual(mergesort(self.test2), self.sorted2)

  def test_bubbleSort(self):
    self.assertEqual(bubblesort(self.test1), self.sorted1)
    self.assertEqual(bubblesort(self.test2), self.sorted2)

  def test_quickSort(self):
    self.assertEqual(quicksort(self.test1), self.sorted1)
    self.assertEqual(quicksort(self.test2), self.sorted2)

if __name__ == '__main__':
  unittest.main()