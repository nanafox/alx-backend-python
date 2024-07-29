import unittest
from unittest.mock import MagicMock, patch

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
