#!/usr/bin/env python3

"""This module contains unit tests for the GithubOrgClient class."""

import unittest
from unittest.mock import MagicMock, PropertyMock, patch

from parameterized import parameterized

import client as github_client


class TestGithubOrgClient(unittest.TestCase):
    """This class tests the GithubOrgClient class."""

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """Test that the org method returns the expected output."""
        mock_get_json.return_value = MagicMock(return_value=expected)
        client = github_client.GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test that the _public_repos_url property returns the expected
        output."""
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                github_client.GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
