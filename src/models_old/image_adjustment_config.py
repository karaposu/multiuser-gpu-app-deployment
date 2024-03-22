# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.image_adjustment_config_asd import ImageAdjustmentConfigASD


class ImageAdjustmentConfig(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ImageAdjustmentConfig - a model defined in OpenAPI

        asd: The asd of this ImageAdjustmentConfig [Optional].
        return_img_format: The return_img_format of this ImageAdjustmentConfig [Optional].
    """

    asd: Optional[ImageAdjustmentConfigASD] = Field(alias="ASD", default=None)
    return_img_format: Optional[str] = Field(alias="return_img_format", default=None)

ImageAdjustmentConfig.update_forward_refs()
