#!/usr/bin/env python3
"""utils.access_nested_map function
"""

from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that inherits from unittest.TestCase
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, input1, input2, result):
        """Method to test that the method returns the access
        nested map with key path"""
        self.assertEqual(access_nested_map(input1, input2), result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, input1, input2, result):
        """Method to test that the method returns the access
        nested map with key path"""
        with self.assertRaises(KeyError):
            access_nested_map(input1, input2)


class TestGetJson(unittest.TestCase):
    """TestGetJson class that inherits from unittest.TestCase
    and test the get_json method
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, result):
        """Test that the get_json method returns the expected result
        """
        mocked_response = Mock()
        mocked_response.json.return_value = result
        with patch('requests.get', return_value=mocked_response) as mocked_get:
            self.assertEqual(get_json(url), result)
            mocked_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """TestGetJson class that inherits from unittest.TestCase
    and test the memoize method
    """
    def test_memoize(self):
        """Tests `memoize`'s output.
        """
        class TestClass:
            """Class test"""

            def a_method(self):
                """A method test"""
                return 42

            @memoize
            def a_property(self):
                """A method test"""
                return self.a_method()

        with patch.object(
            TestClass,
            'a_method',
            return_value=42
        ) as mocked_method:
            c1 = TestClass()
            self.assertEqual(c1.a_property, 42)
            self.assertEqual(c1.a_property, 42)
            mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
