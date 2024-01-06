#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        """ To unit-test GithubOrgClient.public_repos. """
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
    def test_public_repos(self, mocked_json: MagicMock) -> None:
        """ To unit-test GithubOrgClient.public_repos. """
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected_return):
        """ To unit-test GithubOrgClient.has_license. """
        self.assertEqual(
            GithubOrgClient.has_license(repo, key), expected_return)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
