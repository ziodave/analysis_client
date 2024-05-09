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

from analysis_client.models.entity import Entity

class TestEntity(unittest.TestCase):
    """Entity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Entity:
        """Test Entity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Entity`
        """
        model = Entity()
        if include_optional:
            return Entity(
                entity_id = '',
                confidence = 1.337,
                main_type = '',
                types = [
                    ''
                    ],
                label = '',
                description = '',
                images = [
                    ''
                    ],
                same_as = [
                    ''
                    ],
                properties = analysis_client.models.properties.Properties(
                    latitude = 1.337, 
                    longitude = 1.337, ),
                synonyms = [
                    ''
                    ]
            )
        else:
            return Entity(
        )
        """

    def testEntity(self):
        """Test Entity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
