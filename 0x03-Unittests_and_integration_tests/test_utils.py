#!/usr/bin/env python3
""" File executable path """

from utils import access_nested_map, get_json, memoize
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
""" Module import path """


class TestAccessNestedMap(TestCase):
    """ Class that inherits from unittest.TestCase """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Method that returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the nested map"),
        ({"a": 1}, ("a", "b"),
            "Key 'b' not found in the nested map under key 'a'")
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_error_message):
        """ Method to ensure that the exception message is as expected """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_error_message)


class TestGetJson(TestCase):
    """ TestGetJson(unittest.TestCase) class """

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Method to test that utils.get_json returns the expected result """
        response = Mock()
        response.json.return_value = test_payload
        mock_get.return_value = response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(TestCase):
    """ TestMemoize(unittest.TestCase) class with a test_memoize method """

    def test_memoize(self):
        """ A test_memoize that holds a class """

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_one = TestClass()
            object_one = test_one.a_property()
            object_two = test_one.a_property()
            mock_a_method.assert_called_once()
            self.assertEqual(object_one, 42)
            self.assertEqual(object_one, 42)
