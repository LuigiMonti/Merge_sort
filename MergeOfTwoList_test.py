import unittest

from MergeOfTwoList import merge_two_lists


class TestMergeTwoLists(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            merge_two_lists([1, 2, 4], [1, 3, 4]),
            [1, 1, 2, 3, 4, 4]
        )

    def test_empty_lists(self):
        self.assertEqual(merge_two_lists([], []), [])

    def test_one_empty(self):
        self.assertEqual(merge_two_lists([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merge_two_lists([], [4, 5]), [4, 5])

    def test_no_overlap(self):
        self.assertEqual(
            merge_two_lists([1, 2, 3], [4, 5, 6]),
            [1, 2, 3, 4, 5, 6]
        )

    def test_duplicates(self):
        self.assertEqual(
            merge_two_lists([1, 1, 1], [1, 1]),
            [1, 1, 1, 1, 1]
        )

    def test_negative_numbers(self):
        self.assertEqual(
            merge_two_lists([-3, -1, 2], [-2, 0, 3]),
            [-3, -2, -1, 0, 2, 3]
        )

    def test_already_sorted_requirement(self):
        # Este test asegura que funciona correctamente con listas ordenadas
        self.assertEqual(
            merge_two_lists([0, 5, 10], [1, 2, 3]),
            [0, 1, 2, 3, 5, 10]
        )


if __name__ == "__main__":
    unittest.main()