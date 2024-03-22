# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class OperationStatus2(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    OperationStatus2 - a model defined in OpenAPI

        success: The success of this OperationStatus2 [Optional].
        error_code: The error_code of this OperationStatus2 [Optional].
        debug_log: The debug_log of this OperationStatus2 [Optional].
        package_sent_time: The package_sent_time of this OperationStatus2 [Optional].
        extra_field: The extra_field of this OperationStatus2 [Optional].
    """

    success: Optional[bool] = Field(alias="success", default=None)
    error_code: Optional[str] = Field(alias="error_code", default=None)
    debug_log: Optional[str] = Field(alias="debug_log", default=None)
    package_sent_time: Optional[str] = Field(alias="package_sent_time", default=None)
    extra_field: Optional[str] = Field(alias="extra_field", default=None)

OperationStatus2.update_forward_refs()
