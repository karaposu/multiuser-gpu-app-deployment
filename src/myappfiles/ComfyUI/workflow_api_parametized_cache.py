from dotenv import load_dotenv
import os
import random
import sys
from typing import Sequence, Mapping, Any, Union
import torch
from time import time

# script_dir = os.path.dirname(__file__)  # Directory where the script is located
# sys.path.append(os.path.join(script_dir, '..', '..', '..'))  # Adjust the path accordingly

script_dir = os.path.dirname(__file__)  # Directory of the current script
print("script_dir: ", script_dir)
sys.path.append(script_dir)  # Appe


# script_dir = os.path.dirname(__file__)  # Directory of the current script
# print("script_dir: ", script_dir)
# comfy_ui_dir = os.path.join(script_dir, '..')  # Adjust this path as necessary
# print("comfy_ui_dir: ", comfy_ui_dir)
# sys.path.append(comfy_ui_dir)


from nodes import CheckpointLoaderSimple
from data_access_impl import LocalModelLoader, GoogleCloudStorageModelLoader

load_dotenv()
environment = os.getenv('APP_ENVIRONMENT')
bucket_name = os.getenv('GOOGLE_CLOUD_STORAGE_BUCKET')



def get_value_at_index(obj: Union[Sequence, Mapping], index: int) -> Any:
    """Returns the value at the given index of a sequence or mapping.

    If the object is a sequence (like list or string), returns the value at the given index.
    If the object is a mapping (like a dictionary), returns the value at the index-th key.

    Some return a dictionary, in these cases, we look for the "results" key

    Args:
        obj (Union[Sequence, Mapping]): The object to retrieve the value from.
        index (int): The index of the value to retrieve.

    Returns:
        Any: The value at the given index.

    Raises:
        IndexError: If the index is out of bounds for the object and the object is not a mapping.
    """
    try:
        return obj[index]
    except KeyError:
        return obj["result"][index]


def find_path(name: str, path: str = None) -> str:
    """
    Recursively looks at parent folders starting from the given path until it finds the given name.
    Returns the path as a Path object if found, or None otherwise.
    """
    # If no path is given, use the current working directory
    if path is None:
        path = os.getcwd()

    # Check if the current directory contains the name
    if name in os.listdir(path):
        path_name = os.path.join(path, name)
        print(f"{name} found: {path_name}")
        return path_name

    # Get the parent directory
    parent_directory = os.path.dirname(path)

    # If the parent directory is the same as the current directory, we've reached the root and stop the search
    if parent_directory == path:
        return None

    # Recursively call the function with the parent directory
    return find_path(name, parent_directory)


def add_comfyui_directory_to_sys_path() -> None:
    """
    Add 'ComfyUI' to the sys.path
    """
    comfyui_path = find_path("ComfyUI")
    if comfyui_path is not None and os.path.isdir(comfyui_path):
        sys.path.append(comfyui_path)
        print(f"'{comfyui_path}' added to sys.path")


def add_extra_model_paths() -> None:
    """
    Parse the optional extra_model_paths.yaml file and add the parsed paths to the sys.path.
    """
    from main import load_extra_path_config

    extra_model_paths = find_path("extra_model_paths.yaml")

    if extra_model_paths is not None:
        load_extra_path_config(extra_model_paths)
    else:
        print("Could not find the extra_model_paths config file.")

# add_comfyui_directory_to_sys_path()

# add_extra_model_paths()
# t02 = time()
# print("--------add_extra_model_paths  >>>>>  ", t02 - t01)
from nodes import (
    CLIPTextEncode,
    SaveImage,
    VAEDecode,
    KSampler,
    EmptyLatentImage,
)



def main(text, filename_prefix, dependency_container=None):
    # CLIPTextEncode= dependency_container.CLIPTextEncode
    # SaveImage=dependency_container.SaveImage
    # VAEDecode=dependency_container.VAEDecode
    # KSampler=dependency_container.KSampler
    # EmptyLatentImage=dependency_container.EmptyLatentImage

    if dependency_container:
        with torch.inference_mode():
            checkpointloadersimple_4 = dependency_container.cached_checkpoint
            cliptextencode_negative = CLIPTextEncode()
            cliptextencode_positive= CLIPTextEncode()
            emptylatentimage = EmptyLatentImage()
            ksampler =dependency_container.ksampler
            vaedecode = dependency_container.vaedecode
            saveimage = dependency_container.saveimage
            emptylatentimage_5 = emptylatentimage.generate( width=512, height=512, batch_size=1 )

            if dependency_container.fixed_positive_prompt:
               # cliptextencode_6=dependency_container.cliptextencode_6
                cliptextencode_6=dependency_container.encoded_positive_cliptext
            else:
                cliptextencode_6 = cliptextencode_positive.encode(text=text, clip=get_value_at_index(checkpointloadersimple_4, 1),  )
            if dependency_container.fixed_negative_prompt:
                #cliptextencode_7 = dependency_container.cliptextencode_7
                cliptextencode_7 = dependency_container.encoded_negative_cliptext
            else:
                cliptextencode_7= cliptextencode_positive.encode(text="text, watermark", clip=get_value_at_index(checkpointloadersimple_4, 1), )

            for q in range(1):
                ksampler_3 = ksampler.sample(
                    seed=random.randint(1, 2**64),
                    steps=20,
                    cfg=8,
                    sampler_name="euler",
                    scheduler="normal",
                    denoise=1,
                    model=get_value_at_index(checkpointloadersimple_4, 0),
                    positive=get_value_at_index(cliptextencode_6, 0),
                    negative=get_value_at_index(cliptextencode_7, 0),
                    latent_image=get_value_at_index(emptylatentimage_5, 0),
                )

                vaedecode_8 = vaedecode.decode(
                    samples=get_value_at_index(ksampler_3, 0),
                    vae=get_value_at_index(checkpointloadersimple_4, 2),
                )

                images=get_value_at_index(vaedecode_8, 0)
                saveimage_9 = saveimage.save_images(
                    filename_prefix=filename_prefix, images=images
                )

            return images

    else:

        with torch.inference_mode():


            if environment == "original_code" :
               checkpointloadersimple = CheckpointLoaderSimple()
            elif environment == "development":
                checkpointloadersimple = LocalModelLoader()
            elif environment == "cloud" :
                checkpointloadersimple = GoogleCloudStorageModelLoader(bucket_name=bucket_name)

            checkpointloadersimple_4 = checkpointloadersimple.load_checkpoint(
                ckpt_name="dreamshaper_8.safetensors"
            )

            emptylatentimage = EmptyLatentImage()

            emptylatentimage_5 = emptylatentimage.generate(
                width=512, height=512, batch_size=1
            )

            cliptextencode = CLIPTextEncode()

            cliptextencode_6 = cliptextencode.encode(
                text=text,
                clip=get_value_at_index(checkpointloadersimple_4, 1),
            )

            cliptextencode_7 = cliptextencode.encode(
                text="text, watermark",
                clip=get_value_at_index(checkpointloadersimple_4, 1),
            )

            ksampler = KSampler()
            vaedecode = VAEDecode()
            saveimage = SaveImage()


            for q in range(1):
                ksampler_3 = ksampler.sample(
                    seed=random.randint(1, 2**64),
                    steps=20,
                    cfg=8,
                    sampler_name="euler",
                    scheduler="normal",
                    denoise=1,
                    model=get_value_at_index(checkpointloadersimple_4, 0),
                    positive=get_value_at_index(cliptextencode_6, 0),
                    negative=get_value_at_index(cliptextencode_7, 0),
                    latent_image=get_value_at_index(emptylatentimage_5, 0),
                )

                vaedecode_8 = vaedecode.decode(
                    samples=get_value_at_index(ksampler_3, 0),
                    vae=get_value_at_index(checkpointloadersimple_4, 2),
                )

                images=get_value_at_index(vaedecode_8, 0)
                saveimage_9 = saveimage.save_images(
                    filename_prefix=filename_prefix, images=images
                )
                # t11 = time()
                # print("--------11  >>>>>  ", t11 - t10)
            print("------type images", type(images))
            images = images.cpu().numpy()
            print("------type images", type(images))
            print("------shape images", images.shape)



            return images



if __name__ == "__main__":
    text_description = "beautiful scenery nature glass bottle landscape, purple galaxy bottle,"
    filename_prefix = "ComfyUI"
    from cache_model import load_model

    st = time()

    add_extra_model_paths()
    add_comfyui_directory_to_sys_path()


    class DependencyContainer:
        def __init__(self, fixed_positive_prompt=None, fixed_negative_prompt=None ):
            from nodes import (
                CLIPTextEncode,
                SaveImage,
                VAEDecode,
                KSampler,
                EmptyLatentImage,
            )
            self.fixed_positive_prompt=fixed_positive_prompt
            self.fixed_negative_prompt = fixed_negative_prompt
            self.CLIPTextEncode=CLIPTextEncode
            self.SaveImage =SaveImage
            self.VAEDecode =VAEDecode
            self.KSampler= KSampler
            self.EmptyLatentImage= EmptyLatentImage

            self.cached_checkpoint = None

            self.cached_checkpoint =load_model("")
            self.ksampler=KSampler()
            self.vaedecode=VAEDecode()
            self.saveimage = SaveImage()
            self.cliptextencode_negative = CLIPTextEncode()
            self.cliptextencode_positive = CLIPTextEncode()
            self.encoded_positive_cliptext= None
            self.encoded_negative_cliptext = None

            if fixed_positive_prompt:
                self.encoded_positive_cliptext=self.cliptextencode_positive.encode(
                    text=fixed_positive_prompt, clip=get_value_at_index(self.cached_checkpoint, 1)
                )
            if fixed_negative_prompt:
                self.encoded_negative_cliptext=self.cliptextencode_negative.encode(
                    text=fixed_negative_prompt, clip=get_value_at_index(self.cached_checkpoint, 1)
                )


    t1 = time()
    dependency_container = DependencyContainer()
    # dependency_container.cached_checkpoint=load_model("")
    t2 = time()
    print("--------dependency_container init time", t2 - t1)
    # print("--------all time", t2 - st)



    main(text=text_description, filename_prefix=filename_prefix, dependency_container=dependency_container)
