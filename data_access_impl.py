from data_access_interfaces import ImageStorage, ModelLoader, TextStorage
# from abc import ABC, abstractmethod
from typing import Any

from nodes import CheckpointLoaderSimple  # Ensure this import path is correct

from google.cloud import storage
import os

print()


class LocalModelLoader(ModelLoader):
    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        # Using CheckpointLoaderSimple to load the model checkpoint
        return CheckpointLoaderSimple().load_checkpoint(ckpt_name, output_vae=output_vae, output_clip=output_clip)


# class LocalModelLoader(ModelLoader):
#     def __init__(self):
#         # Initialize the cache as an empty dictionary
#         self.cache = {}
#
#     def _generate_cache_key(self, model_name, output_vae, output_clip):
#         # Create a unique key for each combination of model and its configurations
#         return f"{model_name}_vae={output_vae}_clip={output_clip}"
#
#     def load_checkpoint(self, model_name, output_vae=True, output_clip=True):
#         # Generate a unique key for the current request
#         cache_key = self._generate_cache_key(model_name, output_vae, output_clip)
#
#         # Check if the model is already in the cache
#         if cache_key in self.cache:
#             print("Loading model from cache.")
#             return self.cache[cache_key]
#
#         # If not in cache, load the model
#         model_data = CheckpointLoaderSimple().load_checkpoint(model_name, output_vae=output_vae, output_clip=output_clip)
#
#         # Store the loaded model in the cache
#         self.cache[cache_key] = model_data
#
#         return model_data


# import cloud_sdk  # This should be the SDK for your specific cloud provider


# export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
class GoogleCloudStorageModelLoader(ModelLoader):
    def __init__(self, bucket_name, cache_dir=None):
        self.bucket_name = bucket_name
        self.cache_dir = cache_dir if cache_dir else "model_cache"
        os.makedirs(self.cache_dir, exist_ok=True)  # Ensure cache directory exists
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket_name)
        self.cache = {}

    def _generate_cache_key(self, model_name, output_vae, output_clip):
        return f"{model_name}_vae={output_vae}_clip={output_clip}"

    def _download_model_from_cloud(self, model_name):
        local_path = os.path.join(self.cache_dir, model_name)
        blob = self.bucket.blob(model_name)
        blob.download_to_filename(local_path)
        return local_path

    def load_checkpoint(self, model_name, output_vae=True, output_clip=True):
        cache_key = self._generate_cache_key(model_name, output_vae, output_clip)

        # Check cache first
        if cache_key in self.cache:
            print("Loading model from cache.")
            return self.cache[cache_key]

        # If not in cache, download the model
        local_model_path = self._download_model_from_cloud(model_name)

        # Load the model using CheckpointLoaderSimple or another appropriate method
        # Assuming CheckpointLoaderSimple or equivalent can load from the local path
        model_data = CheckpointLoaderSimple().load_checkpoint(local_model_path, output_vae=output_vae, output_clip=output_clip)

        # Update cache
        self.cache[cache_key] = model_data

        return model_data




# Concrete classes for local storage
class LocalImageStorage(ImageStorage):
    def save_image(self, filename_prefix: str, images: Any) -> Any:
        # Implement local image saving logic
        pass

    def retrieve_image(self, filename_prefix: str) -> Any:
        # Implement local image retrieval logic
        pass



class LocalTextStorage(TextStorage):
    def save_text(self, filename: str, text: str) -> Any:
        # Implement local text saving logic
        pass

    def retrieve_text(self, filename: str) -> Any:
        # Implement local text retrieval logic
        pass


# Concrete classes for cloud storage
class CloudImageStorage(ImageStorage):
    def save_image(self, filename_prefix: str, images: Any) -> Any:
        # Implement cloud image saving logic
        pass

    def retrieve_image(self, filename_prefix: str) -> Any:
        # Implement cloud image retrieval logic
        pass


class CloudModelLoader(ModelLoader):
    def load_model(self, model_name: str) -> Any:
        # Implement cloud model loading logic
        pass


class CloudTextStorage(TextStorage):
    def save_text(self, filename: str, text: str) -> Any:
        # Implement cloud text saving logic
        pass

    def retrieve_text(self, filename: str) -> Any:
        # Implement cloud text retrieval logic
        pass
