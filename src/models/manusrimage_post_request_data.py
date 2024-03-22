# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class MANUSRIMAGEPostRequestData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MANUSRIMAGEPostRequestData - a model defined in OpenAPI

        user_image: The user_image of this MANUSRIMAGEPostRequestData.
    """

    user_image: str = Field(alias="user_image")

MANUSRIMAGEPostRequestData.update_forward_refs()