#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, patch, PropertyMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class that inherits from unittest.TestCase."""

    @parameterized.expand([
        ('google', {"org": 'google'}),
        ('abc', {"org": 'abc'})
    ])
    @patch("client.get_json")
    def test_org(
        self, input: str,
        result: Dict,
        mocked_get: MagicMock
    ) -> None:
        """_summary_

        Args:
            org (str): _description_
            expected_response (Dict): _description_
            mocked_function (MagicMock): _description_
        """
        mocked_response = Mock()
        mocked_response.return_value = result
        mocked_get.return_value = mocked_response
        new_client = GithubOrgClient(input)
        self.assertEqual(new_client.org(), result)
        mocked_get.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(input)
        )

    def test_public_repos_url(self):
        payload = {
            "repos_url": "https://github.com/ChinenyeNmoh/alx-backend-python"
        }
        with patch(
            'client.GithubOrgClient.org',
            return_value=payload,
            new_callable=PropertyMock
        ) as mocked_get:
            new_obj = GithubOrgClient('google')
            self.assertEqual(
                new_obj._public_repos_url,
                "https://github.com/ChinenyeNmoh/alx-backend-python"

            )

    @patch('client.get_json')
    def test_public_repos(self, mocked_json):
        payload = {
            'repos_url': "https://github.com/ChinenyeNmoh/alx-backend-python",
            'repos': [
                {"name": "Chinenye"},
                {"name": "Nmoh"}
            ]
        }

        mocked_json.return_value = payload['repos']

        with patch(
            'client.GithubOrgClient._public_repos_url',
            return_value=payload['repos_url'],
            new_callable=PropertyMock
        ) as mocked_get:
            new_obj2 = GithubOrgClient('google')
            self.assertEqual(
                new_obj2.public_repos(),
                [i['name'] for i in payload['repos']]
                )
            mocked_json.assert_called_once()
            mocked_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
