import unittest
import main


class ArraySortTest(unittest.TestCase):
    # TEST NORMAL
    def test_normal_bubble(self):
        expect = [1, 2, 3, 4, 5, 6]
        x = main.Array([3, 4, 2, 1, 6, 5]).bubbleSort()
        self.assertEqual(expect, x)

    def test_normal_quick(self):
        expect = [1, 2, 3, 4, 5, 6]
        x = main.Array([3, 4, 2, 1, 6, 5]).quickSort()
        self.assertEqual(expect, x)

    # TEST NORMAL NEG
    def test_normal_neg_bubble(self):
        expect = [-0.1, 0, 0.1]
        x = main.Array([0.1, -0.1, 0]).bubbleSort()
        self.assertEqual(expect, x)

    def test_normal_neg_quick(self):
        expect = [-0.1, 0, 0.1]
        x = main.Array([0.1, -0.1, 0]).quickSort()
        self.assertEqual(expect, x)

    # TEST NORMAL DOUBLE
    def test_normal_double_bubble(self):
        expect = [0.1, 0.2, 0.3]
        x = main.Array([0.2, 0.1, 0.3]).bubbleSort()
        self.assertEqual(expect, x)

    def test_normal_double_quick(self):
        expect = [0.1, 0.2, 0.3]
        x = main.Array([0.2, 0.1, 0.3]).quickSort()
        self.assertEqual(expect, x)

    # TEST ERROR
    def test_error_bubble(self):
        with self.assertRaises(TypeError):
            x = main.Array([1, "abc", 3, 4, 5]).bubbleSort()

    def test_error_quick(self):
        with self.assertRaises(TypeError):
            x = main.Array([1, "abc", 3, 4, 5]).quickSort()

    # TEST SAME
    def test_same_bubble(self):
        expect = [25, 25]
        x = main.Array([25, 25]).bubbleSort()
        self.assertEqual(expect, x)

    def test_same_quick(self):
        expect = [25, 25]
        x = main.Array([25, 25]).quickSort()
        self.assertEqual(expect, x)

    # TEST EMPTY
    def test_empty_bubble(self):
        expect = []
        x = main.Array([]).bubbleSort()
        self.assertEqual(expect, x)

    def test_empty_quick(self):
        expect = []
        x = main.Array([]).bubbleSort()
        self.assertEqual(expect, x)
