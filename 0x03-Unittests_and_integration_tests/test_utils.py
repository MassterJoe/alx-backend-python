#!/usr/bin/env python3
"""
 write the first unit test for utils.access_nested_map
"""


import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any
)
from utils import access_nested_map, get_json
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """ TestAceessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """test with asserequal"""
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """ to test for exceptions """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ to test getJson class  """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, moke_get_requests):
        """ test get_json """
        moke_get_requests.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        moke_get_requests.assert_called_once_with(test_url)
