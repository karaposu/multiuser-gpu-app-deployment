# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.bug_report_request_data import BugReportRequestData
from models.operation import Operation


class BugReportRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    BugReportRequest - a model defined in OpenAPI

        operation: The operation of this BugReportRequest [Optional].
        data: The data of this BugReportRequest [Optional].
    """

    operation: Optional[Operation] = Field(alias="operation", default=None)
    data: Optional[BugReportRequestData] = Field(alias="data", default=None)

BugReportRequest.update_forward_refs()
