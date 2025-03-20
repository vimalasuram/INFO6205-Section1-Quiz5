import unittest
from selection_sort import SelectionSort
from random import shuffle

class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        self.sorter = SelectionSort()
    
    def test_empty_array(self):
        arr = []
        self.sorter.selection_sort(arr)
        self.assertEqual(arr, [])
        self.assertTrue(self.sorter.is_sorted(arr))
    
    def test_single_element(self):
        arr = [1]
        self.sorter.selection_sort(arr)
        self.assertEqual(arr, [1])
        self.assertTrue(self.sorter.is_sorted(arr))
    
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.sorter.selection_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        self.assertTrue(self.sorter.is_sorted(arr))
    
    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        self.sorter.selection_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        self.assertTrue(self.sorter.is_sorted(arr))
    
    def test_random_array(self):
        arr = list(range(10))
        shuffle(arr)
        original = arr.copy()
        self.sorter.selection_sort(arr)
        self.assertEqual(arr, sorted(original))
        self.assertTrue(self.sorter.is_sorted(arr))
    
    def test_array_with_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.sorter.selection_sort(arr)
        self.assertEqual(arr, sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
        self.assertTrue(self.sorter.is_sorted(arr))
    
    def test_custom_comparator(self):
        # Reverse order comparator
        reverse_comparator = lambda a, b: -1 if a > b else 1 if a < b else 0
        sorter = SelectionSort(reverse_comparator)
        
        arr = [1, 2, 3, 4, 5]
        sorter.selection_sort(arr)
        self.assertEqual(arr, [5, 4, 3, 2, 1])
        self.assertTrue(sorter.is_sorted(arr))
    
    def test_with_strings(self):
        arr = ["banana", "apple", "cherry", "date", "elderberry"]
        self.sorter.selection_sort(arr)
        self.assertEqual(arr, ["apple", "banana", "cherry", "date", "elderberry"])
        self.assertTrue(self.sorter.is_sorted(arr))

if __name__ == '__main__':
    unittest.main()