#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, patch
from parameterized import parameterized

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


if __name__ == '__main__':
    unittest.main()
