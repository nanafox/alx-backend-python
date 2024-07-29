#!/usr/bin/env python3


"""This module contains unit tests for the utils module."""

import unittest

from parameterized import parameterized

import utils


class TestAccessNestedMap(unittest.TestCase):
    """This class tests the access_nested_map function."""

    @parameterized.expand(
        [
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a", "b"], 2),
            ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that the function returns the expected output."""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ["a"]),
            ({"a", 1}, ["a", "b"]),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that the function raises a KeyError for invalid keys."""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
