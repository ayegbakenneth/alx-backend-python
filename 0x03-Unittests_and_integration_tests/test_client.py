#!/usr/bin/env python3
""" File executable path """

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
""" Module importation path """


class TestGithubOrgClient(unittest.TestCase):
    """ Class that implement the test_org method."""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        mock_get_json.return_value = {'login': 'test_org'}
        client = GithubOrgClient(org_name)
        recieved = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(recieved, {'login': 'test_org'})

    @patch('client.GithubOrgClient.org', new_callable=MagicMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url returns the correct value.
        """
        mock_org.return_value = {'repos_url': 'https://api.github.com/orgs/test_org/repos'}
        client = GithubOrgClient('test_org')
        recieved = client._public_repos_url
        self.assertEqual(recieved,'https://api.github.com/orgs/test_org/repos')
