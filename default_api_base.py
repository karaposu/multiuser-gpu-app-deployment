# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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


    def m_andomimage_post(
        self,
        mandomimage_post_request: MANDOMIMAGEPostRequest,
    ) -> DOMImageManipulationResponse:
        ...


    def m_anusrimage_post(
        self,
        manusrimage_post_request: MANUSRIMAGEPostRequest,
    ) -> UserImageManipulationResponse:
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
