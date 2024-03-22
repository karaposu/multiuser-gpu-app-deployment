# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class LMCoordinates(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LMCoordinates - a model defined in OpenAPI

        betweeneyes: The betweeneyes of this LMCoordinates [Optional].
        nose_coordinats: The nose_coordinats of this LMCoordinates.
        cheek_coordinates: The cheek_coordinates of this LMCoordinates.
        chin_coordinates: The chin_coordinates of this LMCoordinates.
        eye_distance: The eye_distance of this LMCoordinates.
        eyegap_chin_distance: The eyegap_chin_distance of this LMCoordinates.
    """

    betweeneyes: Optional[List[int]] = Field(alias="betweeneyes", default=None)
    nose_coordinats: List[int] = Field(alias="nose_coordinats")
    cheek_coordinates: List[int] = Field(alias="cheek_coordinates")
    chin_coordinates: List[int] = Field(alias="chin_coordinates")
    eye_distance: int = Field(alias="eye_distance")
    eyegap_chin_distance: int = Field(alias="eyegap_chin_distance")

LMCoordinates.update_forward_refs()
