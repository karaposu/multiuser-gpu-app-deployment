# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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

class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    def healthcheck(
        self,
    ) -> None:
        ...


    def image_manipulator(
        self,
        x_api_key: str,
        image_manipulation_request: ImageManipulationRequest,
    ) -> ImageManipulationResponse:
        ...


    def increase_user_limit(
        self,
        x_api_key: str,
        increase_user_limit_request: IncreaseUserLimitRequest,
    ) -> IncreaseUserLimit200Response:
        ...


    def register_user(
        self,
        register_user_request: RegisterUserRequest,
    ) -> RegisterUser200Response:
        ...


    def report_bug_post(
        self,
        bug_report_request: BugReportRequest,
    ) -> ShareResultPost200Response:
        ...


    def share_result_post(
        self,
        share_result_request: ShareResultRequest,
    ) -> ShareResultPost200Response:
        ...


    def source_monitoring(
        self,
        x_api_key: str,
    ) -> None:
        ...


    def text_to_image_generator(
        self,
        x_api_key: str,
        image_generation_request: ImageGenerationRequest,
    ) -> ImageGenerationResponse:
        ...


    def v1_image_manipulations_user_post(
        self,
        v1_image_manipulations_user_post_request: V1ImageManipulationsUserPostRequest,
    ) -> UserImageManipulationResponse:
        ...


    def v1_image_manipulations_web_post(
        self,
        v1_image_manipulations_web_post_request: V1ImageManipulationsWebPostRequest,
    ) -> DOMImageManipulationResponse:
        ...
