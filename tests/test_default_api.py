# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error_response import ErrorResponse  # noqa: F401
from openapi_server.models.image_generation_request import ImageGenerationRequest  # noqa: F401
from openapi_server.models.image_generation_response import ImageGenerationResponse  # noqa: F401
from openapi_server.models.image_manipulation_request import ImageManipulationRequest  # noqa: F401
from openapi_server.models.image_manipulation_response import ImageManipulationResponse  # noqa: F401
from openapi_server.models.increase_user_limit200_response import IncreaseUserLimit200Response  # noqa: F401
from openapi_server.models.increase_user_limit_request import IncreaseUserLimitRequest  # noqa: F401
from openapi_server.models.register_user200_response import RegisterUser200Response  # noqa: F401
from openapi_server.models.register_user_request import RegisterUserRequest  # noqa: F401


def test_healthcheck(client: TestClient):
    """Test case for healthcheck

    healtcheck
    """

    headers = {
        "ApiKeyAuth": "special-key",
    }
    response = client.request(
        "GET",
        "/healthcheck",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_image_manipulator(client: TestClient):
    """Test case for image_manipulator

    Process an image according to specified parameters.
    """
    image_manipulation_request = {"data":[{"image":"image","text":"text"},{"image":"image","text":"text"}],"operation":{"operation_name":"operation_name","package_sent_time":"package_sent_time","link":"https://openapi-generator.tech","counter":0,"userid":"userid"},"config":{"settings":[{"setting2":"setting2","setting1":"setting1"},{"setting2":"setting2","setting1":"setting1"}]}}

    headers = {
        "x_api_key": 'x_api_key_example',
        "ApiKeyAuth": "special-key",
    }
    response = client.request(
        "POST",
        "/image-manipulation",
        headers=headers,
        json=image_manipulation_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_increase_user_limit(client: TestClient):
    """Test case for increase_user_limit

    Increase user's limit upon payment.
    """
    increase_user_limit_request = openapi_server.IncreaseUserLimitRequest()

    headers = {
        "x_api_key": 'x_api_key_example',
        "ApiKeyAuth": "special-key",
    }
    response = client.request(
        "POST",
        "/increase-limit",
        headers=headers,
        json=increase_user_limit_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_register_user(client: TestClient):
    """Test case for register_user

    Register a new user.
    """
    register_user_request = openapi_server.RegisterUserRequest()

    headers = {
        "ApiKeyAuth": "special-key",
    }
    response = client.request(
        "POST",
        "/register",
        headers=headers,
        json=register_user_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_source_monitoring(client: TestClient):
    """Test case for source_monitoring

    source monitoring for Disk space and, memory usage, GPU usage,  queue lengths
    """

    headers = {
        "x_api_key": 'x_api_key_example',
        "ApiKeyAuth": "special-key",
    }
    response = client.request(
        "GET",
        "/source-monitoring",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_text_to_image_generator(client: TestClient):
    """Test case for text_to_image_generator

    Process an image according to specified parameters.
    """
    image_generation_request = {"data":"data","operation":{"operation_name":"operation_name","package_sent_time":"package_sent_time","link":"https://openapi-generator.tech","counter":0,"userid":"userid"},"config":{"settings":[{"setting2":"setting2","setting1":"setting1"},{"setting2":"setting2","setting1":"setting1"}]}}

    headers = {
        "x_api_key": 'x_api_key_example',
        "ApiKeyAuth": "special-key",
    }
    response = client.request(
        "POST",
        "/text-to-image-generation",
        headers=headers,
        json=image_generation_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

