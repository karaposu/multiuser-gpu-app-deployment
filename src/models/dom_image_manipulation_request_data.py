# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.headswap_source_obj import HeadswapSourceObj


class DOMImageManipulationRequestData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DOMImageManipulationRequestData - a model defined in OpenAPI

        source_headswap_objs: The source_headswap_objs of this DOMImageManipulationRequestData.
        target_image: The target_image of this DOMImageManipulationRequestData.
    """

    source_headswap_objs: List[HeadswapSourceObj] = Field(alias="source_headswapObjs")
    target_image: str = Field(alias="target_image")

DOMImageManipulationRequestData.update_forward_refs()
