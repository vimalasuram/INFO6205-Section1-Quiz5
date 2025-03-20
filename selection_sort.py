from typing import List, TypeVar, Callable, Optional

T = TypeVar('T')  # Generic type parameter

class SelectionSort:
    """ 
    SelectionSort implementation that can sort arrays of any type.
    This implementation uses a selection sort algorithm which has O(n²) time complexity.
    """

    def __init__(self, comparator: Optional[Callable[[T, T], int]] = None):
        """ 
        Initialize a SelectionSort instance.

        Args:
            comparator: Optional function that compares two elements. 
                        If None, the < operator is used for comparison.
        """
        self.comparator = comparator
        self.comparisons = 0
        self.swaps = 0

    def _less(self, v: T, w: T) -> bool:
        """ 
        Check if v is less than w.

        Args:
            v: First element to compare
            w: Second element to compare

        Returns:
            True if v is less than w, False otherwise
        """
        self.comparisons += 1
        if self.comparator is None:
            return v < w
        else:
            return self.comparator(v, w) < 0

    def _exch(self, arr: List[T], i: int, j: int):
        """ 
        Exchange the elements at positions i and j in the array.

        Args:
            arr: The array to modify
            i: First position
            j: Second position
        """
        self.swaps += 1
        arr[i], arr[j] = arr[j], arr[i]

    def selection_sort(self, arr: List[T]):
        """ 
        Sort the array using selection sort.

        Args:
            arr: The array to sort
        """
        n = len(arr)
        for i in range(n):
            # Find the smallest element in the unsorted part
            min_index = i
            for j in range(i + 1, n):
                if self._less(arr[j], arr[min_index]):
                    min_index = j

            # Swap the found minimum element with the first unsorted element
            if min_index != i:
                self._exch(arr, i, min_index)

    def is_sorted(self, arr: List[T]) -> bool:
        """ 
        Check if the array is sorted.

        Args:
            arr: The array to check

        Returns:
            True if the array is sorted, False otherwise
        """
        for i in range(1, len(arr)):
            if self._less(arr[i], arr[i-1]):
                return False
        return True
