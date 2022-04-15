import unittest

import list_analysis


class TransformToStringTestCase(unittest.TestCase):
    def test_transform_list(self):
        input_data = [1, "a", 10.1]
        self.assertEqual(
            list_analysis.transform_items_to_string(input_data),
            ["1", "a", "10.1"]
        )

    def test_transform_not_list(self):
        self.assertFalse(
            list_analysis.transform_items_to_string(10)
        )

    def test_transform_string(self):
        self.assertFalse(
            list_analysis.transform_items_to_string("100")
        )

    def test_transform_int(self):
        input_data = [1, "a", 10.1]
        self.assertEqual(
            list_analysis.transform_items_to_int(input_data),
            [1, 10]
        )

class CountOccurencesTestCase(unittest,TestCase):
    def test_invalid_input(self):
        self.assertFalse(list_analysis.count_occurences({1, 2, 3}))

    def test_empty_list(self):
        self.assertEqual(list_analysis.count_occurences([]), {})

    def test_nonempty_list(self):
        data = [13, 32, 48, 42, 68, 70, 11, 13, 42, 42, 42, 42]
        expected_result = {13:2, 32:1, 48:1. 68:1, 70:1, 11:1, 42:5}
        self.assertEqual
        self.assertDictEqual(list_analysis.count_occurences(data), expected_result)

