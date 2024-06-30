from unittest import TestCase

from falgopy.sorting.algorithms.quick_sort.quick_sort import QuickSort
from falgopy.sorting.sorting_algorithm.sorting_algorithm_input import SortingAlgorithmInput
from falgopy.sorting.sorting_algorithm.sorting_algorithm_output import SortingAlgorithmOutput


class TestQuickSort(TestCase):
    def test_sort(self):
        for test_input, test_output in self.get_inputs():
            self.assertEqual(QuickSort(test_input).run().sorted_list, test_output.sorted_list)

    @staticmethod
    def get_inputs():
        return [
            (SortingAlgorithmInput(list_to_sort=[-100, -6, 100, -5, 9, -4, -1, 21, 30, 101]),
             SortingAlgorithmOutput(sorted_list=[-100, -6, -5, -4, -1, 9, 21, 30, 100, 101], total_iterations=9))]
