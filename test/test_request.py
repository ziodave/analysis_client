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

from analysis_client.models.request import Request

class TestRequest(unittest.TestCase):
    """Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Request:
        """Test Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Request`
        """
        model = Request()
        if include_optional:
            return Request(
                html = analysis_client.models.html.Html(
                    fragment = '', 
                    page = '', ),
                url = '',
                url_client = 'CHROME',
                language = '01',
                text = '',
                exclude = [
                    ''
                    ],
                scope = '',
                matches = 56,
                links = ''
            )
        else:
            return Request(
                language = '01',
                scope = '',
        )
        """

    def testRequest(self):
        """Test Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
