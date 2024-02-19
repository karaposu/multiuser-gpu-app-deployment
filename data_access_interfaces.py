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
    def load_checkpoint(self, model_name, output_vae=True, output_clip=True):
        pass


class TextStorage(ABC):
    @abstractmethod
    def save_text(self, filename: str, text: str) -> Any:
        pass

    @abstractmethod
    def retrieve_text(self, filename: str) -> Any:
        pass
