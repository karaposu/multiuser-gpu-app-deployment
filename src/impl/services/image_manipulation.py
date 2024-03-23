from .utils import decode_img, encode_img
from myappfiles.dummy_base64_img_returner import base64_img
from time import time

from models.dom_image_manipulation_response_data import DOMImageManipulationResponseData
from models.user_image_manipulation_response_data import UserImageManipulationResponseData
from models.images_datafor_user_image_manipulation_response import ImagesDataforUserImageManipulationResponse
from models.image_result import ImageResult
from models.images_data import ImagesData

from .base_service import BaseService

class UsrImageManipulationService(BaseService):
    def preprocess_request_data(self):

        config = self.request.config
        data = self.request.data
        operation = self.request.operation

        return_img_format=config["return_img_format"]
        user_image = data["user_image"]
        img = decode_img(user_image)

        head = self.dependencies.HeadSwapObj(img, self.dependencies.iie,  used_as_source=True)
        # head = HeadSwapObj(img, iie)
        COMPATIBLE, details = head.check_compatibility()
        COMPATIBLE= True


        # if config["return_img_format"] == "encoded":
        #     i
        unpacked = {"COMPATIBLE": COMPATIBLE,
                             "head": head,
                             "details": details}
        self.preprocessed_data=unpacked


    def head_extraction(self):

        COMPATIBLE = self.preprocessed_data["COMPATIBLE"]
        source = self.preprocessed_data["head"]
        encoded_result_image = None

        if COMPATIBLE:
            HE = self.dependencies.HeadMaskCreator(source, CROP_Head=True, logger=None)
            source = HE.headswapObj

        elapsed_time=0
        return (COMPATIBLE, ""),  source, elapsed_time

    def process_request(self):

        (COMPATIBLE, details), source, elapsed_time = self.head_extraction()

        image_result=ImagesDataforUserImageManipulationResponse(head=source.head,
                                          headselection_mask=source.headselection_mask,
                                          head_transparent=source.head_transparent)


        response_data = UserImageManipulationResponseData(images=image_result,
                                                              fd_coordinates=source.FD_coordinates,
                                                              skin_color=source.skin_color,
                                                              lm_coordinates=source.LM_coordinates )
        self.response=response_data



class ImageManipulationService(BaseService):
    def check_compatibility(self, img, text):
        return True,""
    def preprocess_request_data(self):

        img = self.request.data[0].image
        if img=="string" :
            img= base64_img
        else:
            img = decode_img(img)
        txt = self.request.data[0].text

        COMPATIBLE, details  = self.check_compatibility(img, txt)

        unpacked_dom_data = {"COMPATIBLE": COMPATIBLE,
                             "img": img,
                             "txt": txt}
        self.preprocessed_data=unpacked_dom_data


    def make_image_manipulation(self):

        if self.preprocessed_data["COMPATIBLE"]:
            pass
        else:
            pass

        return base64_img, 10

    def process_request(self):
        encoded_result_image, elapsed_time = self.make_image_manipulation()

        image_result=[ImageResult(result=encoded_result_image)]
        self.response = ImagesData(images=image_result, total_time=10)
        return  self.response

class DomImageManipulationService(BaseService):
    def preprocess_request_data(self):
        config = self.request.config
        data = self.request.data

        source1_data = data["source_headswapObjs"][0]
        source_pose1 = self.make_headswapObj_from_json(source1_data, self.iie, encoded=True)
        # source_pose2 = self.make_headswapObj_from_json(source1_data, iie, encoded=True)
        # source_pose3 = self.make_headswapObj_from_json(source1_data, iie, encoded=True)

        if config["return_img_format"] == "encoded":
            img = decode_img(data["target_image"])

            target = self.dependencies.HeadSwapObj(img, self.dependencies.HeadSwapObj.iie)
            time3 = time()

            COMPATIBLE, details = target.check_compatibility()

        unpacked_dom_data = {"COMPATIBLE": COMPATIBLE,
                                 "target": target,
                                 "source_pose1": source_pose1}

        self.preprocessed_data = unpacked_dom_data


    def make_headswap(self):

        # unpacked_dom_data = unpack_dom_image_package(self)
        COMPATIBLE = self.preprocessed_data["COMPATIBLE"]
        target = self.preprocessed_data["target"]
        source_pose1 = self.preprocessed_data["source_pose1"]

        encoded_result_image = None

        if COMPATIBLE:
            target.tick_compatibility()

            HS = self.dependencies.HeadSwapper(source_pose1, target, self.dependencies.ch, debugging=False, logger=None)
            time4 = time()
            encoded_result_image = encode_img(HS.result)
            time5 = time()
        else:
            pass

        details=""
        elapsed_time=0
        return (COMPATIBLE, details), encoded_result_image, elapsed_time

    def process_request(self):
        if self.compatible:
            (COMPATIBLE, details), encoded_result_image, elapsed_time = self.make_headswap()
            # List[ImageResult]
            image_result=[ImageResult(result=encoded_result_image)]
            dom_response_data = DOMImageManipulationResponseData(images=image_result, total_time="")
            self.response = dom_response_data
            return dom_response_data

    def make_headswapObj_from_json(self, headswapObj_json, iie, encoded=True):
        img=decode_img(headswapObj_json["head_img"])

        headswapObj = self.dependencies.HeadSwapObj(
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
        headswapObj.COMPATIBLE_IMAGE= True
        headswapObj.skincolor_CALCULATED= True
        return headswapObj

#
# def make_headswapObj_from_json(headswapObj_json, iie, encoded=True):
#     img=decode_img(headswapObj_json["head_img"])
#
#     headswapObj = HeadSwapObj(
#         img,
#         iie,
#         FD_coordinates=headswapObj_json["FD_coordinates"],
#         LM_coordinates=headswapObj_json["LM_coordinates"],
#         headselection_mask=decode_img(headswapObj_json["headselection_mask"], mask=True),
#         skincolor=headswapObj_json["skincolor"]
#     )
#     headswapObj.betweeneyes_coordinates = headswapObj_json["LM_coordinates"]["betweeneyes"]
#     headswapObj.nose_coordinates = headswapObj_json["LM_coordinates"]["nose_coordinats"]
#     headswapObj.cheek_coordinates = headswapObj_json["LM_coordinates"]["cheek_coordinates"]
#     headswapObj.chin_coordinates = headswapObj_json["LM_coordinates"]["chin_coordinates"]
#     headswapObj.eye_distance = headswapObj_json["LM_coordinates"]["eye_distance"]
#     headswapObj.eyegap_chin_distance = headswapObj_json["LM_coordinates"]["eyegap_chin_distance"]
#     headswapObj.FACE_EXIST=True
#     headswapObj.LM_CALCULATED=True
#     headswapObj.LANDMARK_EXIST=True
#     HeadSwapObj.COMPATIBLE_IMAGE= True
#     HeadSwapObj.skincolor_CALCULATED= True
#     return headswapObj
#
#
#
# def unpack_user_image_package(package_content):
#
#     return unpacked_user_data
#
#
# def unpack_dom_image_package(package_content,iie):
#     config=package_content.config
#     data = package_content.data
#
#     source1_data = data["source_headswapObjs"][0]
#     source_pose1 = make_headswapObj_from_json(source1_data, iie, encoded=True)
#     # source_pose2 = make_headswapObj_from_json(source1_data, iie, encoded=True)
#     # source_pose3 = make_headswapObj_from_json(source1_data, iie, encoded=True)
#
#     if config["return_img_format"] == "encoded":
#
#         img = decode_img(data["target_image"])
#
#         target = HeadSwapObj(img, iie)
#         time3 = time()
#
#         COMPATIBLE, details = target.check_compatibility()
#
#     unpacked_dom_data= {"COMPATIBLE":COMPATIBLE,
#                         "target":target,
#                         "source_pose1": source_pose1  }
#     return unpacked_dom_data
#
# def make_headswap(iie, ch, package_content, logger):
#
#         unpacked_dom_data=unpack_dom_image_package(package_content, iie)
#         COMPATIBLE=unpacked_dom_data["COMPATIBLE"]
#         target = unpacked_dom_data["target"]
#         source_pose1 = unpacked_dom_data["source_pose1"]
#
#         encoded_result_image = None
#
#         if COMPATIBLE:
#             target.tick_compatibility()
#
#             HS = HeadSwapper(source_pose1, target, ch, debugging=False, logger=logger)
#             time4 = time()
#             encoded_result_image = encode_img(HS.result)
#             time5 = time()
#         else:
#             pass
#
#     # elapsed_time["Total_ImgOp_Time"] = round(time5 - time0, 3)
#     # # elapsed_time["data_processing_start_time"] = time0
#     # elapsed_time["source_heads_creation"] = round(time1 - time0, 3)
#     # elapsed_time["decoding_target_img"] = round(time2 - time1, 3)
#     # elapsed_time["creating_target_headswapObj"] = round(time3 - time2, 3)
#     # elapsed_time["headswapping"] = round(time4 - time3, 3)
#     # elapsed_time["encoding_result_img"] = round(time5 - time4, 3)
#
#     return (COMPATIBLE, details), encoded_result_image, elapsed_time
#
#
#
#
#
# def process_dom_image_manipulation_request(mandomimage_post_request):
#     DATA_IS_VALID, unpacked_data = unpack_dom_image_package(mandomimage_post_request)
#     if DATA_IS_VALID:
#         (COMPATIBLE, details), encoded_result_image, elapsed_time =make_headswap(iie, ch, unpacked_data, logger)
#
#         #def make_headswap(iie, ch, package_content, logger):
#
#
#
# def digest_package_content_and_make_headswap(iie, ch, config, data, logger):
#     # ASD, domain, source_headswapObjs, format, mode, data, package_sent_time = package_content
#
#     elapsed_time = OrderedDict()
#     time0 = time()
#
#     source1_data = data["source_headswapObjs"][0]
#     source_pose1 = make_headswapObj_from_json(source1_data, iie, encoded=True)
#     # source_pose2 = make_headswapObj_from_json(source1_data, iie, encoded=True)
#     # source_pose3 = make_headswapObj_from_json(source1_data, iie, encoded=True)
#
#     time1 = time()
#
#     if config["return_img_format"] == "encoded":
#
#         img = decode_img(data["target_image"])
#         time2 = time()
#
#         target = HeadSwapObj(img, iie)
#         time3 = time()
#
#         COMPATIBLE, details = target.check_compatibility()
#         encoded_result_image = None
#
#         if COMPATIBLE:
#             target.tick_compatibility()
#
#             HS = HeadSwapper(source_pose1, target, ch, debugging=False, logger=logger)
#             time4 = time()
#             encoded_result_image = encode_img(HS.result)
#             time5 = time()
#         else:
#             pass
#
#     elapsed_time["Total_ImgOp_Time"] = round(time5 - time0, 3)
#     # elapsed_time["data_processing_start_time"] = time0
#     elapsed_time["source_heads_creation"] = round(time1 - time0, 3)
#     elapsed_time["decoding_target_img"] = round(time2 - time1, 3)
#     elapsed_time["creating_target_headswapObj"] = round(time3 - time2, 3)
#     elapsed_time["headswapping"] = round(time4 - time3, 3)
#     elapsed_time["encoding_result_img"] = round(time5 - time4, 3)
#
#     return (COMPATIBLE, details), encoded_result_image, elapsed_time
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def unpack_dom_image_package(package_content):
#     # Logic to unpack the incoming package content for DOM images
#     # For example:
#     # Unpacking logic specific to DOM images...
#     # Unpacked_dom_data = ...
#
#     # Returning the unpacked DOM data
#     return unpacked_dom_data
#
#
# def encode_img_to_base64(img):
#     _, img_buffer = cv2.imencode('.webp', img)
#     encoded_img = base64.b64encode(img_buffer)
#     # return encoded_img
#     return encoded_img.decode('utf-8')
#
#
# def decode_base64_to_img(encoded_img,mask=False):
#
#     decoded_img = base64.b64decode(encoded_img)
#
#     img_np_arr = np.frombuffer(decoded_img, np.uint8)
#     if mask:
#         img = cv2.imdecode(img_np_arr,cv2.IMREAD_UNCHANGED)
#         if img is not None and len(img.shape) == 3 and img.shape[2] == 2:
#             pass
#         else:
#             img= img[:,:,2]
#     else:
#          img = cv2.imdecode(img_np_arr, cv2.IMREAD_COLOR)
#     return img
#
# def manipulate_image(img) :
#     # Imagine this function generates an image based on the text and returns the image data
#     # For simplicity, we're just returning a string representing the image data
#
#     #main(text=text, filename_prefix="a")
#     return img
#
# def generate_cabinit_usr_img_man_data_response(base64_encoded_img,pos_prompt,neg_prompt)->ImagesData:
#     image_results=generate_image_results(base64_encoded_img,pos_prompt,neg_prompt)
#
#     images_data = ImagesData(
#         images=image_results,
#         total_time=20  # Example total processing time
#     )
#
#     return images_data
#
# def generate_cabinit_dom_img_man_data_response(data,config)->ImagesData:
#
#
#     image_results=generate_image_results(base64_encoded_img,pos_prompt,neg_prompt)
#
#     images_data = ImagesData(
#         images=image_results,
#         total_time=20  # Example total processing time
#     )
#
#     return images_data
#
#
# def generate_image_data_response(base64_encoded_img,pos_prompt,neg_prompt)->ImagesData:
#     image_results=generate_image_results(base64_encoded_img,pos_prompt,neg_prompt)
#
#     images_data = ImagesData(
#         images=image_results,
#         total_time=20  # Example total processing time
#     )
#
#     return images_data
#
# def generate_image_results(base64_encoded_img,pos_prompt,neg_prompt ):
#     print("incoming encoded image has len: ",len(base64_encoded_img))
#     base64_encoded_img=base64_encoded_img
#
#     if len(base64_encoded_img) < 20:
#         print("using demo encoded image")
#         base64_encoded_img=base64_img.encode()
#         print("incoming encoded image has len: ", len(base64_encoded_img))
#
#     image = decode_base64_to_img(base64_encoded_img)
#
#     #print("3----------------------------------------------")
#
#     #cv2.imwrite('savedImage.jpg', image)
#
#     new_image = manipulate_image(image)
#     new_image_base64_encoded=encode_img_to_base64(new_image)
#
#     image_results = [
#         ImageResult(result=new_image_base64_encoded)
#
#     ]
#     return image_results
#
#
#
 # elapsed_time["Total_ImgOp_Time"] = round(time5 - time0, 3)
    # # elapsed_time["data_processing_start_time"] = time0
    # elapsed_time["source_heads_creation"] = round(time1 - time0, 3)
    # elapsed_time["decoding_target_img"] = round(time2 - time1, 3)
    # elapsed_time["creating_target_headswapObj"] = round(time3 - time2, 3)
    # elapsed_time["headswapping"] = round(time4 - time3, 3)
    # elapsed_time["encoding_result_img"] = round(time5 - time4, 3)
