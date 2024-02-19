from abc import ABC, abstractmethod
from typing import Any


class ImageStorage(ABC):
    @abstractmethod
    def save_image(self, filename_prefix: str, images: Any) -> Any:
        pass

    @abstractmethod
    def retrieve_image(self, filename_prefix: str) -> Any:
        pass


class ModelLoader(ABC):
    @abstractmethod
    def load_model(self, model_name: str) -> Any:
        pass


class TextStorage(ABC):
    @abstractmethod
    def save_text(self, filename: str, text: str) -> Any:
        pass

    @abstractmethod
    def retrieve_text(self, filename: str) -> Any:
        pass
