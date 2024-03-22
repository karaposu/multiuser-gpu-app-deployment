# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from apis.default_api_base import BaseDefaultApi
import impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from models.extra_models import TokenModel  # noqa: F401
from models.error_response import ErrorResponse
from models.increase_user_limit200_response import IncreaseUserLimit200Response
from models.increase_user_limit_request import IncreaseUserLimitRequest
from models.register_extension200_response import RegisterExtension200Response
from models.register_extension_request import RegisterExtensionRequest
from security_api import get_token_ApiKeyAuth

from impl.text_to_image import generate_image_data_response
from impl.image_manipulator import  generate_image_data_response
from impl.source_monitor  import prepare_response_for_source_monitoring
from impl.register_new_user import register_new_user

from models.images_data import ImagesData
from models.image_result import ImageResult
from models.operation_status import OperationStatus

router = APIRouter()

ns_pkg = impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/increase-limit",
    responses={
        200: {"model": IncreaseUserLimit200Response, "description": "Limit increase successful."},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        401: {"model": ErrorResponse, "description": "Unauthorized. Authentication credentials are missing or invalid."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Increase user&#39;s limit upon payment.",
    response_model_by_alias=True,
)
async def increase_user_limit(
    x_api_key: str = Header(None, description="API key needed to authorize requests."),
    increase_user_limit_request: IncreaseUserLimitRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> IncreaseUserLimit200Response:
    ...


@router.post(
    "/register",
    responses={
        200: {"model": RegisterExtension200Response, "description": "Registration successful."},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Register a new Chrome extension installation.",
    response_model_by_alias=True,
)
async def register_extension(
    register_extension_request: RegisterExtensionRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> RegisterExtension200Response:
    user_id = register_new_user(register_extension_request)
    return RegisterExtension200Response(userId=user_id, message="Registration successful")

