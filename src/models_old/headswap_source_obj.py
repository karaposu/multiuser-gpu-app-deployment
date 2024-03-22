# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.lm_coordinates import LMCoordinates


class HeadswapSourceObj(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    HeadswapSourceObj - a model defined in OpenAPI

        head_img: The head_img of this HeadswapSourceObj.
        headselection_mask: The headselection_mask of this HeadswapSourceObj.
        fd_coordinates: The fd_coordinates of this HeadswapSourceObj.
        lm_coordinates: The lm_coordinates of this HeadswapSourceObj.
    """

    head_img: str = Field(alias="head_img")
    headselection_mask: str = Field(alias="headselection_mask")
    fd_coordinates: List[int] = Field(alias="FD_coordinates")
    lm_coordinates: LMCoordinates = Field(alias="LM_coordinates")

HeadswapSourceObj.update_forward_refs()