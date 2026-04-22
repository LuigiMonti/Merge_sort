import unittest

from Merge_sort import merge_sort, merge_two_lists


class TestMergeFunctions(unittest.TestCase):

    def test_merge_two_lists_normal(self):
        self.assertEqual(
            merge_two_lists([1, 2, 4], [1, 3, 4]),
            [1, 1, 2, 3, 4, 4]
        )

    def test_merge_two_lists_empty(self):
        self.assertEqual(merge_two_lists([], []), [])

    def test_merge_two_lists_one_empty(self):
        self.assertEqual(merge_two_lists([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merge_two_lists([], [4, 5]), [4, 5])

    def test_merge_two_lists_negatives(self):
        self.assertEqual(
            merge_two_lists([-3, -1, 2], [-2, 0, 3]),
            [-3, -2, -1, 0, 2, 3]
        )

    def test_merge_sort_normal(self):
        self.assertEqual(
            merge_sort([38, 27, 43, 3, 9, 82, 10]),
            [3, 9, 10, 27, 38, 43, 82]
        )

    def test_merge_sort_empty(self):
        self.assertEqual(merge_sort([]), [])

    def test_merge_sort_single_element(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_merge_sort_already_sorted(self):
        self.assertEqual(
            merge_sort([1, 2, 3, 4]),
            [1, 2, 3, 4]
        )

    def test_merge_sort_reverse(self):
        self.assertEqual(
            merge_sort([5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5]
        )

    def test_merge_sort_duplicates(self):
        self.assertEqual(
            merge_sort([4, 1, 3, 1, 2]),
            [1, 1, 2, 3, 4]
        )


if __name__ == "__main__":
    unittest.main()