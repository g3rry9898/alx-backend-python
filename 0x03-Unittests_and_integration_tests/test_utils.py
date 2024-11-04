#!/usr/bin/env python3

import unittest
from parametized import parametized
from utils import acess_nested_map

class TestAccessNestedMap(unittest.Testcase):

    @parametized.expand([nested_map={"a": 1}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a", "b")])

    def test_access_nested_map(nested_map, path, expected):

        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == "__main__":
    unittest.main()


