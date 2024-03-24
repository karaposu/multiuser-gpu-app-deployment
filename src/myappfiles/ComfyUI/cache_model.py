from data_access_impl import LocalModelLoader, GoogleCloudStorageModelLoader
def load_model(ckpt_name):
    print("---------------load_model")
    checkpointloadersimple = LocalModelLoader()
    checkpointloadersimple_4 = checkpointloadersimple.load_checkpoint(
        ckpt_name="dreamshaper_8.safetensors"
    )
    return checkpointloadersimple_4


# from cache_model import load_model