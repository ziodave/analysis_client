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

from analysis_client.models.entity_gap_request import EntityGapRequest

class TestEntityGapRequest(unittest.TestCase):
    """EntityGapRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntityGapRequest:
        """Test EntityGapRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntityGapRequest`
        """
        model = EntityGapRequest()
        if include_optional:
            return EntityGapRequest(
                url = '',
                query = '',
                model = '',
                number_of_entities = 56,
                query_location_name = 'United States',
                query_search_engine = 'google.com'
            )
        else:
            return EntityGapRequest(
                url = '',
                query = '',
        )
        """

    def testEntityGapRequest(self):
        """Test EntityGapRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
