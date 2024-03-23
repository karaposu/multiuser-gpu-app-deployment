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

from models.extra_models import TokenModel
from models.bug_report_request import BugReportRequest
from models.dom_image_manipulation_response import DOMImageManipulationResponse
from models.error_response import ErrorResponse
from models.image_generation_request import ImageGenerationRequest
from models.image_generation_response import ImageGenerationResponse
from models.image_manipulation_request import ImageManipulationRequest
from models.image_manipulation_response import ImageManipulationResponse
from models.increase_user_limit200_response import IncreaseUserLimit200Response
from models.increase_user_limit_request import IncreaseUserLimitRequest
from models.mandomimage_post_request import MANDOMIMAGEPostRequest
from models.manusrimage_post_request import MANUSRIMAGEPostRequest
from models.register_user200_response import RegisterUser200Response
from models.register_user_request import RegisterUserRequest
from models.share_result_post200_response import ShareResultPost200Response
from models.share_result_request import ShareResultRequest
from models.user_image_manipulation_response import UserImageManipulationResponse
from security_api import get_token_ApiKeyAuth


from impl.text_to_image import generate_image_data_response_for_text_to_image
from impl.image_manipulator import  generate_image_data_response, generate_cabinit_dom_img_man_data_response, generate_cabinit_usr_img_man_data_response
from impl.source_monitor  import prepare_response_for_source_monitoring
from impl.register_new_user import register_new_user
from impl.request_handler import RequestHandler

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
    rh = RequestHandler()
    return rh.handle_image_manipulation_request(image_manipulation_request)



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
    rh = RequestHandler()
    return rh.handle_increase_user_limit_request(increase_user_limit_request)

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
async def mandomimage_post(
    mandomimage_post_request: MANDOMIMAGEPostRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> DOMImageManipulationResponse:

    rh=RequestHandler()
    return rh.handle_dom_image_manipulation_request(mandomimage_post_request)



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
async def manusrimage_post(
    manusrimage_post_request: MANUSRIMAGEPostRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) -> UserImageManipulationResponse:
    rh = RequestHandler()
    return rh.handle_dom_image_manipulation_request(manusrimage_post_request)


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
    rh = RequestHandler()
    return rh.handle_register_user_request(register_user_request)


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
    rh = RequestHandler()
    return rh.handle_report_bug_request(bug_report_request)


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
    rh = RequestHandler()
    return rh.handle_source_monitoring_request()

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
    rh = RequestHandler()
    return rh.handle_text_to_image_request(image_generation_request)