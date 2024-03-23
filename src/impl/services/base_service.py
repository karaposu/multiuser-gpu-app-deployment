from abc import ABC, abstractmethod

class BaseService(ABC):
    def __init__(self, request, dependencies):
        self.request = request
        self.dependencies = dependencies
        self.unpacked_request = None
        self.response = None

    @abstractmethod
    def unpack_request(self):
        """Unpack and validate the incoming request."""
        pass

    @abstractmethod
    def check_compatibility(self, img=None, text=None):
        """Check if the request is compatible with the service's requirements."""
        pass

    @abstractmethod
    def process_request(self):
        """Process the request and produce a response."""
        pass
