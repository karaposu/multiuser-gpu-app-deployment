# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.operation import Operation
from models.share_result_request_data import ShareResultRequestData


class ShareResultRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ShareResultRequest - a model defined in OpenAPI

        operation: The operation of this ShareResultRequest [Optional].
        data: The data of this ShareResultRequest [Optional].
    """

    operation: Optional[Operation] = Field(alias="operation", default=None)
    data: Optional[ShareResultRequestData] = Field(alias="data", default=None)

ShareResultRequest.update_forward_refs()