# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class BugReportRequestData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    BugReportRequestData - a model defined in OpenAPI

        textfield: The textfield of this BugReportRequestData [Optional].
    """

    textfield: Optional[str] = Field(alias="textfield", default=None)

BugReportRequestData.update_forward_refs()
