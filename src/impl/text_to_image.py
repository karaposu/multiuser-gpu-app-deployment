
from models.images_data import ImagesData
from models.operation_status import OperationStatus
from models.image_result import ImageResult


import cv2
import base64
# from src.myappfiles.workflow_api_parametized import main
from myappfiles.dummy_base64_img_returner import base64_img
def encode_img(img):
    _, img_buffer = cv2.imencode('.webp', img)
    encoded_img = base64.b64encode(img_buffer)
    # return encoded_img
    return encoded_img.decode('utf-8')

def generate_image(text: str) -> str:
    # Imagine this function generates an image based on the text and returns the image data
    # For simplicity, we're just returning a string representing the image data

    #main(text=text, filename_prefix="a")
    return base64_img

def generate_image_response(text: str):
    images = generate_image(text)
    if not isinstance(images[0], str):
        base64_images=encode_img(images[0])
    else:
        base64_images=images
    image_results = [
        ImageResult(result=base64_images),
        ImageResult(result="Image processing result 2"),
        # Add more ImageResult instances as needed
    ]
    return image_results




def generate_image_data_response(text: str)->ImagesData:
    image_results=generate_image_response(text)
    images_data = ImagesData(
        images=image_results,
        total_time=20  # Example total processing time
    )

    return images_data



# def generate_ImagesData(text: str) -> str:
#     # Imagine this function generates an image based on the text and returns the image data
#     # For simplicity, we're just returning a string representing the image data
#     return "image_data_based_on_" + text


# images_data = ImagesData(images=["asdsadsa"], total_time=20)