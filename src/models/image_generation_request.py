# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.config import Config
from models.operation import Operation


class ImageGenerationRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ImageGenerationRequest - a model defined in OpenAPI

        operation: The operation of this ImageGenerationRequest.
        config: The config of this ImageGenerationRequest.
        data: The data of this ImageGenerationRequest.
    """

    operation: Operation = Field(alias="operation")
    config: Config = Field(alias="config")
    data: str = Field(alias="data")

ImageGenerationRequest.update_forward_refs()
