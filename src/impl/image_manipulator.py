
from models.images_data import ImagesData
from models.operation_status import OperationStatus
from models.image_result import ImageResult

from utils import decode_img, encode_img

import cv2
import base64
# from src.myappfiles.workflow_api_parametized import main
from myappfiles.dummy_base64_img_returner import base64_img
import numpy as np
from time import time

from models.dom_image_manipulation_response_data import DOMImageManipulationResponseData
from models.image_result import ImageResult


class ImageManipulationOperation:
    # dom_image_manipulation_operation
    def __init__(self, request, iie):
        self.request = request
        self.iie = iie
        self.unpacked_request = self.unpack_image_manipulation_package()
        self.response= self.process_image_manipulation_request()

    def check_compatibility(self, img, text):
        return True
    def unpack_image_manipulation_package(self):

        img = self.request.data[0].image
        img = decode_img(img)
        txt = self.request.data[0].text

        COMPATIBLE, details  = self.check_compatibility(img, txt)

        unpacked_dom_data = {"COMPATIBLE": COMPATIBLE,
                             "img": img,
                             "txt": txt}
        return unpacked_dom_data

    def make_image_manipulation(self):

        if self.unpacked_request["COMPATIBLE"]:
            pass
        else:
            pass

        return (COMPATIBLE, details), encoded_result_image, elapsed_time

    def process_image_manipulation_request(mandomimage_post_request):
        DATA_IS_VALID, unpacked_data = unpack_dom_image_package(mandomimage_post_request)
        if DATA_IS_VALID:
            (COMPATIBLE, details), encoded_result_image, elapsed_time = make_headswap(iie, ch, unpacked_data, logger)
            # List[ImageResult]
            image_result=[ImageResult(result=encoded_result_image)]
            dom_response_data = DOMImageManipulationResponseData(images=image_result, total_time="")
            return dom_response_data




class DomImageManipulationOperation:
    # dom_image_manipulation_operation
    def __init__(self, mandomimage_post_request, iie):
        self.mandomimage_post_request = mandomimage_post_request
        self.iie = iie
        self.unpacked_dom_data = self.unpack_dom_image_package()
        self.dom_response_data= self.process_dom_image_manipulation_request()

    # DATA_IS_VALID, unpacked_data = unpack_dom_image_package(mandomimage_post_request)
    def unpack_dom_image_package(self):
        config = self.mandomimage_post_request.config
        data = self.mandomimage_post_request.data

        source1_data = data["source_headswapObjs"][0]
        source_pose1 = make_headswapObj_from_json(source1_data, self.iie, encoded=True)
        # source_pose2 = make_headswapObj_from_json(source1_data, iie, encoded=True)
        # source_pose3 = make_headswapObj_from_json(source1_data, iie, encoded=True)

        if config["return_img_format"] == "encoded":
            img = decode_img(data["target_image"])

            target = HeadSwapObj(img, iie)
            time3 = time()

            COMPATIBLE, details = target.check_compatibility()

        unpacked_dom_data = {"COMPATIBLE": COMPATIBLE,
                             "target": target,
                             "source_pose1": source_pose1}
        return unpacked_dom_data

    def make_headswap(iie, ch, package_content, logger):

        unpacked_dom_data = unpack_dom_image_package(package_content, iie)
        COMPATIBLE = unpacked_dom_data["COMPATIBLE"]
        target = unpacked_dom_data["target"]
        source_pose1 = unpacked_dom_data["source_pose1"]

        encoded_result_image = None

        if COMPATIBLE:
            target.tick_compatibility()

            HS = HeadSwapper(source_pose1, target, ch, debugging=False, logger=logger)
            time4 = time()
            encoded_result_image = encode_img(HS.result)
            time5 = time()
        else:
            pass

    # elapsed_time["Total_ImgOp_Time"] = round(time5 - time0, 3)
    # # elapsed_time["data_processing_start_time"] = time0
    # elapsed_time["source_heads_creation"] = round(time1 - time0, 3)
    # elapsed_time["decoding_target_img"] = round(time2 - time1, 3)
    # elapsed_time["creating_target_headswapObj"] = round(time3 - time2, 3)
    # elapsed_time["headswapping"] = round(time4 - time3, 3)
    # elapsed_time["encoding_result_img"] = round(time5 - time4, 3)

        return (COMPATIBLE, details), encoded_result_image, elapsed_time

    def process_dom_image_manipulation_request(mandomimage_post_request):
        DATA_IS_VALID, unpacked_data = unpack_dom_image_package(mandomimage_post_request)
        if DATA_IS_VALID:
            (COMPATIBLE, details), encoded_result_image, elapsed_time = make_headswap(iie, ch, unpacked_data, logger)
            # List[ImageResult]
            image_result=[ImageResult(result=encoded_result_image)]
            dom_response_data = DOMImageManipulationResponseData(images=image_result, total_time="")
            return dom_response_data



def make_headswapObj_from_json(headswapObj_json, iie, encoded=True):
    img=decode_img(headswapObj_json["head_img"])

    headswapObj = HeadSwapObj(
        img,
        iie,
        FD_coordinates=headswapObj_json["FD_coordinates"],
        LM_coordinates=headswapObj_json["LM_coordinates"],
        headselection_mask=decode_img(headswapObj_json["headselection_mask"], mask=True),
        skincolor=headswapObj_json["skincolor"]
    )
    headswapObj.betweeneyes_coordinates = headswapObj_json["LM_coordinates"]["betweeneyes"]
    headswapObj.nose_coordinates = headswapObj_json["LM_coordinates"]["nose_coordinats"]
    headswapObj.cheek_coordinates = headswapObj_json["LM_coordinates"]["cheek_coordinates"]
    headswapObj.chin_coordinates = headswapObj_json["LM_coordinates"]["chin_coordinates"]
    headswapObj.eye_distance = headswapObj_json["LM_coordinates"]["eye_distance"]
    headswapObj.eyegap_chin_distance = headswapObj_json["LM_coordinates"]["eyegap_chin_distance"]
    headswapObj.FACE_EXIST=True
    headswapObj.LM_CALCULATED=True
    headswapObj.LANDMARK_EXIST=True
    HeadSwapObj.COMPATIBLE_IMAGE= True
    HeadSwapObj.skincolor_CALCULATED= True
    return headswapObj



def unpack_user_image_package(package_content):

    return unpacked_user_data


def unpack_dom_image_package(package_content,iie):
    config=package_content.config
    data = package_content.data

    source1_data = data["source_headswapObjs"][0]
    source_pose1 = make_headswapObj_from_json(source1_data, iie, encoded=True)
    # source_pose2 = make_headswapObj_from_json(source1_data, iie, encoded=True)
    # source_pose3 = make_headswapObj_from_json(source1_data, iie, encoded=True)

    if config["return_img_format"] == "encoded":

        img = decode_img(data["target_image"])

        target = HeadSwapObj(img, iie)
        time3 = time()

        COMPATIBLE, details = target.check_compatibility()

    unpacked_dom_data= {"COMPATIBLE":COMPATIBLE,
                        "target":target,
                        "source_pose1": source_pose1  }
    return unpacked_dom_data

def make_headswap(iie, ch, package_content, logger):

        unpacked_dom_data=unpack_dom_image_package(package_content, iie)
        COMPATIBLE=unpacked_dom_data["COMPATIBLE"]
        target = unpacked_dom_data["target"]
        source_pose1 = unpacked_dom_data["source_pose1"]

        encoded_result_image = None

        if COMPATIBLE:
            target.tick_compatibility()

            HS = HeadSwapper(source_pose1, target, ch, debugging=False, logger=logger)
            time4 = time()
            encoded_result_image = encode_img(HS.result)
            time5 = time()
        else:
            pass

    # elapsed_time["Total_ImgOp_Time"] = round(time5 - time0, 3)
    # # elapsed_time["data_processing_start_time"] = time0
    # elapsed_time["source_heads_creation"] = round(time1 - time0, 3)
    # elapsed_time["decoding_target_img"] = round(time2 - time1, 3)
    # elapsed_time["creating_target_headswapObj"] = round(time3 - time2, 3)
    # elapsed_time["headswapping"] = round(time4 - time3, 3)
    # elapsed_time["encoding_result_img"] = round(time5 - time4, 3)

    return (COMPATIBLE, details), encoded_result_image, elapsed_time





def process_dom_image_manipulation_request(mandomimage_post_request):
    DATA_IS_VALID, unpacked_data = unpack_dom_image_package(mandomimage_post_request)
    if DATA_IS_VALID:
        (COMPATIBLE, details), encoded_result_image, elapsed_time =make_headswap(iie, ch, unpacked_data, logger)

        #def make_headswap(iie, ch, package_content, logger):



def digest_package_content_and_make_headswap(iie, ch, config, data, logger):
    # ASD, domain, source_headswapObjs, format, mode, data, package_sent_time = package_content

    elapsed_time = OrderedDict()
    time0 = time()

    source1_data = data["source_headswapObjs"][0]
    source_pose1 = make_headswapObj_from_json(source1_data, iie, encoded=True)
    # source_pose2 = make_headswapObj_from_json(source1_data, iie, encoded=True)
    # source_pose3 = make_headswapObj_from_json(source1_data, iie, encoded=True)

    time1 = time()

    if config["return_img_format"] == "encoded":

        img = decode_img(data["target_image"])
        time2 = time()

        target = HeadSwapObj(img, iie)
        time3 = time()

        COMPATIBLE, details = target.check_compatibility()
        encoded_result_image = None

        if COMPATIBLE:
            target.tick_compatibility()

            HS = HeadSwapper(source_pose1, target, ch, debugging=False, logger=logger)
            time4 = time()
            encoded_result_image = encode_img(HS.result)
            time5 = time()
        else:
            pass

    elapsed_time["Total_ImgOp_Time"] = round(time5 - time0, 3)
    # elapsed_time["data_processing_start_time"] = time0
    elapsed_time["source_heads_creation"] = round(time1 - time0, 3)
    elapsed_time["decoding_target_img"] = round(time2 - time1, 3)
    elapsed_time["creating_target_headswapObj"] = round(time3 - time2, 3)
    elapsed_time["headswapping"] = round(time4 - time3, 3)
    elapsed_time["encoding_result_img"] = round(time5 - time4, 3)

    return (COMPATIBLE, details), encoded_result_image, elapsed_time


















def unpack_dom_image_package(package_content):
    # Logic to unpack the incoming package content for DOM images
    # For example:
    # Unpacking logic specific to DOM images...
    # Unpacked_dom_data = ...

    # Returning the unpacked DOM data
    return unpacked_dom_data


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

def generate_cabinit_usr_img_man_data_response(base64_encoded_img,pos_prompt,neg_prompt)->ImagesData:
    image_results=generate_image_results(base64_encoded_img,pos_prompt,neg_prompt)

    images_data = ImagesData(
        images=image_results,
        total_time=20  # Example total processing time
    )

    return images_data

def generate_cabinit_dom_img_man_data_response(data,config)->ImagesData:


    image_results=generate_image_results(base64_encoded_img,pos_prompt,neg_prompt)

    images_data = ImagesData(
        images=image_results,
        total_time=20  # Example total processing time
    )

    return images_data


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



