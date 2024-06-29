# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

class ReadOnlyStates(BaseModel):
    """
    Information about which states the field can be edited in  # noqa: E501
    """
    state_type: constr(strict=True, min_length=1) = Field(..., alias="stateType", description="The State Type (e.g. InitialState, AllStates, TerminalState, SelectedStates)")
    selected_states: Optional[conlist(StrictStr)] = Field(None, alias="selectedStates", description="Named states for which the field will be readonly - This field can only be populated if StateType = SelectedStates")
    __properties = ["stateType", "selectedStates"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ReadOnlyStates:
        """Create an instance of ReadOnlyStates from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if selected_states (nullable) is None
        # and __fields_set__ contains the field
        if self.selected_states is None and "selected_states" in self.__fields_set__:
            _dict['selectedStates'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReadOnlyStates:
        """Create an instance of ReadOnlyStates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReadOnlyStates.parse_obj(obj)

        _obj = ReadOnlyStates.parse_obj({
            "state_type": obj.get("stateType"),
            "selected_states": obj.get("selectedStates")
        })
        return _obj
