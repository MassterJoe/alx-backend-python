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
from utils import access_nested_map


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
