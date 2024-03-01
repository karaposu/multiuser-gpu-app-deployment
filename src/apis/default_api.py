# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil
from fastapi import HTTPException

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
from models.image_generation_request import ImageGenerationRequest
from models.image_generation_response import ImageGenerationResponse
from models.image_manipulation_request import ImageManipulationRequest
from models.image_manipulation_response import ImageManipulationResponse
from models.increase_user_limit200_response import IncreaseUserLimit200Response
from models.increase_user_limit_request import IncreaseUserLimitRequest
from models.register_user200_response import RegisterUser200Response
from models.register_user_request import RegisterUserRequest
from security_api import get_token_ApiKeyAuth

from impl.text_to_image import generate_image_data_response

from models.images_data import ImagesData
from models.operation_status import OperationStatus
from models.image_result import ImageResult
#
router = APIRouter()

ns_pkg = impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/healthcheck",
    responses={
        200: {"description": "healthcheck."},
    },
    tags=["default"],
    summary="healtcheck",
    response_model_by_alias=True,
)
async def healthcheck(
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> None:
    ...


@router.post(
    "/image-manipulation",
    responses={
        200: {"model": ImageManipulationResponse, "description": "Image processed successfully."},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        401: {"model": ErrorResponse, "description": "Unauthorized. Authentication credentials are missing or invalid."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Process an image according to specified parameters.",
    response_model_by_alias=True,
)
async def image_manipulator(
    x_api_key: str = Header(None, description="API key needed to authorize requests."),
    image_manipulation_request: ImageManipulationRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> ImageManipulationResponse:
    ...


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
        200: {"model": RegisterUser200Response, "description": "Registration successful."},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Register a new user.",
    response_model_by_alias=True,
)
async def register_user(
    register_user_request: RegisterUserRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> RegisterUser200Response:
    ...


@router.get(
    "/source-monitoring",
    responses={
        200: {"description": "Image processed successfully."},
    },
    tags=["default"],
    summary="source monitoring for Disk space and, memory usage, GPU usage,  queue lengths",
    response_model_by_alias=True,
)
async def source_monitoring(
    x_api_key: str = Header(None, description="API key needed to authorize requests."),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> None:
    ...


@router.post(
    "/text-to-image-generation",
    responses={
        200: {"model": ImageGenerationResponse, "description": "Image processed successfully."},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        401: {"model": ErrorResponse, "description": "Unauthorized. Authentication credentials are missing or invalid."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Process an image according to specified parameters.",
    response_model_by_alias=True,
)
async def text_to_image_generator(
    x_api_key: str = Header(None, description="API key needed to authorize requests."),
    image_generation_request: ImageGenerationRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security( get_token_ApiKeyAuth ),
) -> ImageGenerationResponse:

    if not image_generation_request.data:
        raise HTTPException(status_code=400, detail="Text for image generation is required")


    images_data=generate_image_data_response(image_generation_request.data)
    ops = OperationStatus(success="true", error_code="",debug_log="", package_sent_time="", counter=12)

    return  ImageGenerationResponse(operation=ops, data=images_data)

