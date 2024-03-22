# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ImageManipulationRequestData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ImageManipulationRequestData - a model defined in OpenAPI

        image: The image of this ImageManipulationRequestData [Optional].
        text: The text of this ImageManipulationRequestData [Optional].
    """

    image: Optional[str] = Field(alias="image", default=None)
    text: Optional[str] = Field(alias="text", default=None)

ImageManipulationRequestData.update_forward_refs()
