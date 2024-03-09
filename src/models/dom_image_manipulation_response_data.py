# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.image_result import ImageResult


class DOMImageManipulationResponseData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DOMImageManipulationResponseData - a model defined in OpenAPI

        images: The images of this DOMImageManipulationResponseData [Optional].
        total_time: The total_time of this DOMImageManipulationResponseData [Optional].
    """

    images: Optional[List[ImageResult]] = Field(alias="images", default=None)
    total_time: Optional[int] = Field(alias="total_time", default=None)

DOMImageManipulationResponseData.update_forward_refs()
