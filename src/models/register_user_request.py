# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.register_user_request_platform import RegisterUserRequestPlatform


class RegisterUserRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RegisterUserRequest - a model defined in OpenAPI

        app_version: The app_version of this RegisterUserRequest.
        installation_id: The installation_id of this RegisterUserRequest.
        timestamp: The timestamp of this RegisterUserRequest.
        locale: The locale of this RegisterUserRequest.
        platform: The platform of this RegisterUserRequest.
    """

    app_version: str = Field(alias="appVersion")
    installation_id: str = Field(alias="installationId")
    timestamp: datetime = Field(alias="timestamp")
    locale: str = Field(alias="locale")
    platform: RegisterUserRequestPlatform = Field(alias="platform")

RegisterUserRequest.update_forward_refs()