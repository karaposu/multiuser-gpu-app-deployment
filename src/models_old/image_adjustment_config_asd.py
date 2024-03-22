# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ImageAdjustmentConfigASD(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ImageAdjustmentConfigASD - a model defined in OpenAPI

        skincolortransfer: The skincolortransfer of this ImageAdjustmentConfigASD [Optional].
        headorientation: The headorientation of this ImageAdjustmentConfigASD [Optional].
        hairtransfer: The hairtransfer of this ImageAdjustmentConfigASD [Optional].
        generic_setting1: The generic_setting1 of this ImageAdjustmentConfigASD [Optional].
        generic_setting2: The generic_setting2 of this ImageAdjustmentConfigASD [Optional].
    """

    skincolortransfer: Optional[int] = Field(alias="skincolortransfer", default=None)
    headorientation: Optional[int] = Field(alias="headorientation", default=None)
    hairtransfer: Optional[int] = Field(alias="hairtransfer", default=None)
    generic_setting1: Optional[int] = Field(alias="generic_setting1", default=None)
    generic_setting2: Optional[int] = Field(alias="generic_setting2", default=None)

ImageAdjustmentConfigASD.update_forward_refs()