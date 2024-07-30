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

    @patch("client.get_json")
    def test_public_repos(self, get_json):
        """Test that the public_repos method returns the expected output."""
        test_payload = {
            'repos_url': "https://api.github.com/users/microsoft/repos",
            'repos': [
                {
                    "id": 123456,
                    "name": "vscode",
                    "private": False,
                    "owner": {
                        "login": "microsoft",
                        "id": 12345,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/microsoft/vscode",
                    "created_at": "2015-01-01T00:00:00Z",
                    "updated_at": "2020-01-01T00:00:00Z",
                    "has_issues": True,
                    "forks": 100,
                    "default_branch": "main",
                },
                {
                    "id": 789012,
                    "name": "TypeScript",
                    "private": False,
                    "owner": {
                        "login": "microsoft",
                        "id": 12345,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/microsoft/TypeScript",
                    "created_at": "2012-01-01T00:00:00Z",
                    "updated_at": "2020-01-01T00:00:00Z",
                    "has_issues": True,
                    "forks": 200,
                    "default_branch": "main",
                },
            ]
        }

        get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                github_client.GithubOrgClient("microsoft").public_repos(),
                ["vscode", "TypeScript"],
            )
            mock_public_repos_url.assert_called_once()
        get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """Test that the has_license method returns the expected output."""
        client = github_client.GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)
