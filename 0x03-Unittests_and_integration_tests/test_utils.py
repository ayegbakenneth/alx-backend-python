#!/usr/bin/env python3
""" File executable path """

import unittest
from parameterized import parameterized
from utils import access_nested_map
""" Module import path """


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class that inherits from unittest.TestCase """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected_result):
        """  method to test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested map under key 'a'")
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected_error_message):
        """ TestAccessNestedMap.test_access_nested_map_exception that use the assertRaises """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_error_message)
