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
from models.bug_report_request import BugReportRequest
from models.dom_image_manipulation_response import DOMImageManipulationResponse
from models.error_response import ErrorResponse
from models.image_generation_request import ImageGenerationRequest
from models.image_generation_response import ImageGenerationResponse
from models.image_manipulation_request import ImageManipulationRequest
from models.image_manipulation_response import ImageManipulationResponse
from models.increase_user_limit200_response import IncreaseUserLimit200Response
from models.increase_user_limit_request import IncreaseUserLimitRequest
from models.register_user200_response import RegisterUser200Response
from models.register_user_request import RegisterUserRequest
from models.share_result_post200_response import ShareResultPost200Response
from models.share_result_request import ShareResultRequest
from models.user_image_manipulation_response import UserImageManipulationResponse
from models.v1_image_manipulations_user_post_request import V1ImageManipulationsUserPostRequest
from models.v1_image_manipulations_web_post_request import V1ImageManipulationsWebPostRequest
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
    return "Healthy", 200


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
    if not image_manipulation_request.data:
        raise HTTPException(status_code=400, detail="Text for image generation is required")
    img = image_manipulation_request.data[0].image
    txt = image_manipulation_request.data[0].text

    images_data = generate_image_data_response(img, txt, "")
    ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)

    return ImageManipulationResponse(operation=ops, data=images_data)


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
    user_id = register_new_user(register_user_request)
    return RegisterUser200Response(userId=user_id, message="Registration successful")


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
    return prepare_response_for_source_monitoring()


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
    if not image_generation_request.data:
        raise HTTPException(status_code=400, detail="Text for image generation is required")

    images_data = generate_image_data_response(image_generation_request.data, "", "")
    ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)

    return ImageGenerationResponse(operation=ops, data=images_data)


@router.post(
    "/v1/image-manipulations/user",
    responses={
        200: {"model": UserImageManipulationResponse, "description": "Image processed successfully."},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        401: {"model": ErrorResponse, "description": "Unauthorized. Authentication credentials are missing or invalid."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Endpoint to handle user image manipulation requests.",
    response_model_by_alias=True,
)
async def v1_image_manipulations_user_post(
    v1_image_manipulations_user_post_request: V1ImageManipulationsUserPostRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> UserImageManipulationResponse:
    ...


@router.post(
    "/v1/image-manipulations/web",
    responses={
        200: {"model": DOMImageManipulationResponse, "description": "Image processed successfully."},
        400: {"model": ErrorResponse, "description": "Bad request. The request body is not correctly structured or contains invalid parameters."},
        401: {"model": ErrorResponse, "description": "Unauthorized. Authentication credentials are missing or invalid."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. An error occurred on the server while processing the request."},
    },
    tags=["default"],
    summary="Endpoint to handle user image manipulation requests.",
    response_model_by_alias=True,
)
async def v1_image_manipulations_web_post(
    v1_image_manipulations_web_post_request: V1ImageManipulationsWebPostRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> DOMImageManipulationResponse:
    ...