import random
import unittest

from sort import *

class TestSort(unittest.TestCase):
  
    def test_insertion_sort(self):        
        data = list("INSERTIONSORT")
        result = insertion_sort(data)
        self.assertEqual(result, ['E', 'I', 'I', 'N', 'N', 'O', 'O', 'R', 'R', 'S', 'S', 'T', 'T'])

    def test_recursive_merge_sort(self):        
        data = [23, 55, 47, 35, 10, 90, 84, 30]
        result = recursive_merge_sort(data)        
        self.assertEqual(result, [10, 23, 30, 35, 47, 55, 84, 90])

    def test_merge_sort(self):        
        data = [23, 55, 47, 35, 10, 90, 84, 30]
        result = merge_sort(data)        
        self.assertEqual(result, [10, 23, 30, 35, 47, 55, 84, 90])

    def test_quick_sort(self):        
        data = [23, 55, 47, 35, 10, 90, 84, 30]
        result = quick_sort(data)        
        self.assertEqual(result, [10, 23, 30, 35, 47, 55, 84, 90])

    # def test_dijkstra_quick_sort(self):        
    #     data = [23, 55, 47, 35, 10, 90, 84, 30]
    #     result = dijkstra_quick_sort(data)        
    #     self.assertEqual(result, [10, 23, 30, 35, 47, 55, 84, 90])

    def test_selection_sort(self):
        data = list("SELECTIONSORT")
        result = selection_sort(data)
        self.assertEqual(result, ['C', 'E', 'E', 'I', 'L', 'N', 'O', 'O', 'R', 'S', 'S', 'T', 'T'])

    def test_shell_sort(self):
        data = list("MOLEEXASPRT")
        result = shell_sort(data)
        self.assertEqual(result, ['A', 'E', 'E', 'L', 'M', 'O', 'P', 'R', 'S', 'T', 'X'])

    def test_knuth_shuffle(self):
        data = list("KNUTHSHUFFLE")
        result = knuth_shuffle(data)
        self.assertNotEqual(result, list("KNUTHSHUFFLE"))

if __name__ == '__main__':
    unittest.main()