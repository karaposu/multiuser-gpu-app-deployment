# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ConfigUserImageManipulation(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ConfigUserImageManipulation - a model defined in OpenAPI

        return_img_format: The return_img_format of this ConfigUserImageManipulation [Optional].
    """

    return_img_format: Optional[str] = Field(alias="return_img_format", default=None)

ConfigUserImageManipulation.update_forward_refs()
