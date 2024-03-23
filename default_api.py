# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

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

from api.models.extra_models import TokenModel  # noqa: F401
from api.models.bug_report_request import BugReportRequest
from api.models.dom_image_manipulation_response import DOMImageManipulationResponse
from api.models.error_response import ErrorResponse
from api.models.image_generation_request import ImageGenerationRequest
from api.models.image_generation_response import ImageGenerationResponse
from api.models.image_manipulation_request import ImageManipulationRequest
from api.models.image_manipulation_response import ImageManipulationResponse
from api.models.increase_user_limit200_response import IncreaseUserLimit200Response
from api.models.increase_user_limit_request import IncreaseUserLimitRequest
from api.models.mandomimage_post_request import MANDOMIMAGEPostRequest
from api.models.manusrimage_post_request import MANUSRIMAGEPostRequest
from api.models.register_user200_response import RegisterUser200Response
from api.models.register_user_request import RegisterUserRequest
from api.models.share_result_post200_response import ShareResultPost200Response
from api.models.share_result_request import ShareResultRequest
from api.models.user_image_manipulation_response import UserImageManipulationResponse
from api.security_api import get_token_ApiKeyAuth

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/health",
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
    "/template/image-manipulation",
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
    "/v1/increase-limit",
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
    "/MAN_DOM_IMAGE/",
    responses={
        200: {"model": DOMImageManipulationResponse, "description": "Image processed successfully."},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        401: {"model": ErrorResponse, "description": "Unauthorized. Authentication credentials are missing or invalid."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Endpoint to handle DOM image manipulation requests.",
    response_model_by_alias=True,
)
async def m_andomimage_post(
    mandomimage_post_request: MANDOMIMAGEPostRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> DOMImageManipulationResponse:
    ...


@router.post(
    "/MAN_USR_IMAGE/",
    responses={
        200: {"model": UserImageManipulationResponse, "description": "Image processed successfully."},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        401: {"model": ErrorResponse, "description": "Unauthorized. Authentication credentials are missing or invalid."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Endpoint to extract head part from the user image.",
    response_model_by_alias=True,
)
async def m_anusrimage_post(
    manusrimage_post_request: MANUSRIMAGEPostRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> UserImageManipulationResponse:
    ...


@router.post(
    "/v1/register",
    responses={
        200: {"model": RegisterUser200Response, "description": "Registration successful."},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        401: {"model": ErrorResponse, "description": "Unauthorized. Authentication credentials are missing or invalid."},
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


@router.post(
    "/report-bug",
    responses={
        200: {"model": ShareResultPost200Response, "description": "Bug report submitted successfully"},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        401: {"model": ErrorResponse, "description": "Unauthorized. Authentication credentials are missing or invalid."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Submit a bug report",
    response_model_by_alias=True,
)
async def report_bug_post(
    bug_report_request: BugReportRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> ShareResultPost200Response:
    ...


@router.post(
    "/share-result",
    responses={
        200: {"model": ShareResultPost200Response, "description": "Bug report submitted successfully"},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        401: {"model": ErrorResponse, "description": "Unauthorized. Authentication credentials are missing or invalid."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Share the result of image processing",
    response_model_by_alias=True,
)
async def share_result_post(
    share_result_request: ShareResultRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> ShareResultPost200Response:
    ...


@router.get(
    "/v1/source-monitoring",
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
    "/v1/text-to-image-generation",
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
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> ImageGenerationResponse:
    ...
