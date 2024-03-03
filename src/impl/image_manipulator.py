
from models.images_data import ImagesData
from models.operation_status import OperationStatus
from models.image_result import ImageResult



import cv2
import base64
# from src.myappfiles.workflow_api_parametized import main
from myappfiles.dummy_base64_img_returner import base64_img
import numpy as np


def encode_img_to_base64(img):
    _, img_buffer = cv2.imencode('.webp', img)
    encoded_img = base64.b64encode(img_buffer)
    # return encoded_img
    return encoded_img.decode('utf-8')


def decode_base64_to_img(encoded_img,mask=False):

    decoded_img = base64.b64decode(encoded_img)

    img_np_arr = np.frombuffer(decoded_img, np.uint8)
    if mask:
        img = cv2.imdecode(img_np_arr,cv2.IMREAD_UNCHANGED)
        if img is not None and len(img.shape) == 3 and img.shape[2] == 2:
            pass
        else:
            img= img[:,:,2]
    else:
         img = cv2.imdecode(img_np_arr, cv2.IMREAD_COLOR)
    return img

def manipulate_image(img) :
    # Imagine this function generates an image based on the text and returns the image data
    # For simplicity, we're just returning a string representing the image data

    #main(text=text, filename_prefix="a")
    return img


def generate_image_data_response(base64_encoded_img,pos_prompt,neg_prompt)->ImagesData:
    image_results=generate_image_results(base64_encoded_img,pos_prompt,neg_prompt)

    images_data = ImagesData(
        images=image_results,
        total_time=20  # Example total processing time
    )

    return images_data

def generate_image_results(base64_encoded_img,pos_prompt,neg_prompt ):
    print("incoming encoded image has len: ",len(base64_encoded_img))
    base64_encoded_img=base64_encoded_img

    if len(base64_encoded_img) < 20:
        print("using demo encoded image")
        base64_encoded_img=base64_img.encode()
        print("incoming encoded image has len: ", len(base64_encoded_img))

    image = decode_base64_to_img(base64_encoded_img)

    #print("3----------------------------------------------")

    #cv2.imwrite('savedImage.jpg', image)

    new_image = manipulate_image(image)
    new_image_base64_encoded=encode_img_to_base64(new_image)

    image_results = [
        ImageResult(result=new_image_base64_encoded)

    ]
    return image_results



