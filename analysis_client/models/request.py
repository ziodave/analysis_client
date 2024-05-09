# coding: utf-8

"""
    Analysis

    Analyse content using Linked Data and Knowledge Graphs.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from analysis_client.models.html import Html
from typing import Optional, Set
from typing_extensions import Self

class Request(BaseModel):
    """
    The request
    """ # noqa: E501
    html: Optional[Html] = None
    url: Optional[StrictStr] = Field(default=None, description="The url of the page to analyze.")
    url_client: Optional[StrictStr] = Field(default=None, description="The client which the analysis should use to extract the content, by default chrome is used.", alias="urlClient")
    language: Annotated[str, Field(min_length=2, strict=True, max_length=2)] = Field(description="The content language, 2 letters code, e.g. 'en'.")
    text: Optional[StrictStr] = Field(default=None, description="A textual fragment.")
    exclude: Optional[List[StrictStr]] = Field(default=None, description="An array of item IDs to exclude from the analysis results.")
    scope: StrictStr = Field(description="The scope of the analysis, one of 'local', 'network', 'cloud-only', 'network-only' or 'all'.")
    matches: Optional[StrictInt] = Field(default=None, description="Filter out results that don't have at least the specified number of occurrences. By default 1.")
    links: Optional[StrictStr] = Field(default=None, description="When returning an interpolated HTML results, matches should have the 'wl-link' class. By default 'no'.")
    __properties: ClassVar[List[str]] = ["html", "url", "urlClient", "language", "text", "exclude", "scope", "matches", "links"]

    @field_validator('url_client')
    def url_client_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CHROME', 'PLAIN_HTTP', 'CHROME, PLAIN_HTTP']):
            raise ValueError("must be one of enum values ('CHROME', 'PLAIN_HTTP', 'CHROME, PLAIN_HTTP')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of html
        if self.html:
            _dict['html'] = self.html.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "html": Html.from_dict(obj["html"]) if obj.get("html") is not None else None,
            "url": obj.get("url"),
            "urlClient": obj.get("urlClient"),
            "language": obj.get("language"),
            "text": obj.get("text"),
            "exclude": obj.get("exclude"),
            "scope": obj.get("scope"),
            "matches": obj.get("matches"),
            "links": obj.get("links")
        })
        return _obj


