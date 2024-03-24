from dotenv import load_dotenv
import os
import random
import sys
from typing import Sequence, Mapping, Any, Union
import torch


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


add_comfyui_directory_to_sys_path()
add_extra_model_paths()

from nodes import (
    CLIPTextEncode,
    SaveImage,
    VAEDecode,
    KSampler,
    EmptyLatentImage,
)


def main(text, filename_prefix, dependency_container=None):

    cached_checkpoint=dependency_container.cached_checkpoint
    t0 = time()

    with torch.inference_mode():
        if not cached_checkpoint:
            print("if not cached_checkpoint-------------")
            if environment == "original_code" :
               checkpointloadersimple = CheckpointLoaderSimple()
            elif environment == "development":
                checkpointloadersimple = LocalModelLoader()
            elif environment == "cloud" :
                checkpointloadersimple = GoogleCloudStorageModelLoader(bucket_name=bucket_name)

            checkpointloadersimple_4 = checkpointloadersimple.load_checkpoint(
                ckpt_name="dreamshaper_8.safetensors"
            )
        else:
            checkpointloadersimple_4=cached_checkpoint
        t1 = time()
        print("--------1  >>>>>  ", t1 - t0)

        emptylatentimage = EmptyLatentImage()
        t2 = time()
        print("--------2  >>>>>  ", t2 - t1)
        emptylatentimage_5 = emptylatentimage.generate(
            width=512, height=512, batch_size=1
        )
        t3 = time()
        print("--------3  >>>>>  ", t3 - t2)
        print(" CLIPTextEncode.encode-------------")
        cliptextencode = CLIPTextEncode()
        t4 = time()
        print("--------4  >>>>>  ", t4 - t3)



        cliptextencode_6 = cliptextencode.encode(
            text=text,
            clip=get_value_at_index(checkpointloadersimple_4, 1),
        )
        t5 = time()
        print("--------5  >>>>>  ", t5 - t4)
        ksampler = KSampler()
        vaedecode = VAEDecode()
        saveimage = SaveImage()
        t6 = time()
        print("--------6  >>>>>  ", t6 - t4)



        cliptextencode_7 = cliptextencode.encode(
            text="text, watermark", clip=get_value_at_index(checkpointloadersimple_4, 1)
        )
        print(" KSampler,VAEDecode,SaveImage-------------")

        t7 = time()
        print("--------7  >>>>>  ", t7 - t6)
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
            t8 = time()
            print("--------8  >>>>>  ", t8 - t7)

            vaedecode_8 = vaedecode.decode(
                samples=get_value_at_index(ksampler_3, 0),
                vae=get_value_at_index(checkpointloadersimple_4, 2),
            )

            t9 = time()
            print("--------9  >>>>>  ", t9 - t8)
            images=get_value_at_index(vaedecode_8, 0)
            t10 = time()
            print("--------10  >>>>>  ", t10 - t9)
            saveimage_9 = saveimage.save_images(
                filename_prefix=filename_prefix, images=images
            )
            t11 = time()
            print("--------11  >>>>>  ", t11 - t10)

            return images



if __name__ == "__main__":
    text_description = "beautiful scenery nature glass bottle landscape, purple galaxy bottle,"
    filename_prefix = "ComfyUI"
    from cache_model import load_model
    from time import time
    class DependencyContainer:
        def __init__(self):
            self.cached_checkpoint = None
            # Initialize other dependencies
            self.otherDependency = None


    dependency_container = DependencyContainer()
    dependency_container.cached_checkpoint=load_model("")

    st=time()
    m=load_model("")
    ft = time()
    print("--------", ft-st)
    print("---------------------------")
    print("---------------------------")


    main(text=text_description, filename_prefix=filename_prefix, dependency_container=dependency_container)
