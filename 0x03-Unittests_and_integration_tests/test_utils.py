#!/usr/bin/env python3


"""This module contains unit tests for the utils module."""

import unittest
import unittest.mock

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


class TestGetJson(unittest.TestCase):
    """This class tests the get_json function."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    def test_get_json(self, url, payload):
        """Test that the function returns the expected output."""
        with unittest.mock.patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual(utils.get_json(url), payload)
