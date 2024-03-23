from datetime import datetime
import uuid
from models.register_user_request import RegisterUserRequest
from models.register_user200_response import RegisterUser200Response

# from models.register_extension_request import RegisterExtensionRequest
# from models.register_extension200_response import RegisterExtension200Response
#
class RegisterOperation:
    def __init__(self, request):
        self.request = request
        self.register_new_user()
        # self.unpacked = self.unpack_user_manipulation_package()
        # self.response = self.process_user_manipulation_request()

    def register_new_user(self) -> RegisterUser200Response:
        """
        Register a new user with the provided details.

        :param request: RegisterUserRequest object containing user registration details.
        :return: RegisterUser200Response object containing the registration response.
        """

        # Here, you would include logic to save the user's details to your database.
        # For demonstration purposes, we'll generate a UUID as the user ID and pretend to save it.

        user_id = str(uuid.uuid4())

        self.user_id=user_id

        # Assuming successful registration, return a response
        # return RegisterUser200Response(userId=user_id, message="Registration successful")
        return user_id