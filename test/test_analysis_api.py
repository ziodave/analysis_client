# coding: utf-8

"""
    Analysis

    Analyse content using Linked Data and Knowledge Graphs.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from analysis_client.api.analysis_api import AnalysisApi


class TestAnalysisApi(unittest.TestCase):
    """AnalysisApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AnalysisApi()

    def tearDown(self) -> None:
        pass

    def test_analyse(self) -> None:
        """Test case for analyse

        Analyse content
        """
        pass

    def test_merge(self) -> None:
        """Test case for merge

        Analyse and Merge
        """
        pass

    def test_v2_analysis(self) -> None:
        """Test case for v2_analysis

        Analyse Web Page
        """
        pass


if __name__ == '__main__':
    unittest.main()
