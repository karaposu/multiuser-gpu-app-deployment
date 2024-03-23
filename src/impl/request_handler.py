from models.images_data import ImagesData
from models.image_result import ImageResult
from models.operation_status import OperationStatus

from models.mandomimage_post_request import MANDOMIMAGEPostRequest
from models.dom_image_manipulation_response import DOMImageManipulationResponse
from models.image_manipulation_response import ImageManipulationResponse
from models.increase_user_limit200_response import IncreaseUserLimit200Response
from models.manusrimage_post_request import MANUSRIMAGEPostRequest
from models.user_image_manipulation_response import UserImageManipulationResponse
from models.increase_user_limit_request import IncreaseUserLimitRequest
from models.register_user_request import RegisterUserRequest
from models.register_user200_response import RegisterUser200Response

from models.image_generation_request import ImageGenerationRequest
from models.image_generation_response import ImageGenerationResponse

from impl.image_manipulator import  DomImageManipulationOperation, ImageManipulationOperation, UsrImageManipulationOperation
from impl.increasing_limit import  IncreaseLimitOperation
from impl.register_new_user import  RegisterOperation
from impl.source_monitor import SourceMonitoringOperation

from impl.text_to_image import TextToImageOperation


from models.bug_report_request import BugReportRequest




from datetime import datetime
from collections import OrderedDict

from models.images_data import ImagesData
from models.image_result import ImageResult
from models.operation_status import OperationStatus

# from settings.utils import(
# digest_package_content_and_extract_head,
# digest_package_content_and_make_headswap,
# prepare_data_dict,
# prepare_data_dict_MAN_DOM,
# prepare_meta_dict,
# check_metadata_validity)

import logging

# werkzeug_logger = logging.getLogger('werkzeug')
# werkzeug_logger.setLevel(logging.WARNING)


class RequestHandler:
    def __init__(self, iie,ch, et=False):
        self.package_content = None
        self.requester_id = None
        self.package_sent_time = None
        self.response = None
        self.iie=iie
        self.ch=ch
        self.DATA_IS_VALID = None
        self.META_IS_VALID = None
        self.USER_HAS_PERMISSION = None

        self.REQUEST_IS_VALID=None
        self.error_code=None

        logger = logging.getLogger(__name__)

        logger.setLevel(logging.DEBUG)
        logger.debug(" ------ ")
        self.logger= logger

        self.elapsed_time =et

        if not self.elapsed_time:

            self.elapsed_time= OrderedDict()

        # self.elapsed_time = OrderedDict()

        # self.elapsed_time["start_time"] = time.time()
    def op_validity(self,meta_data):

        is_permitted=self.check_metadata_validity(meta_data.operation)
        if is_permitted:
            return True
        else:
           # raise HTTPException(status_code=400, detail="user doesnt have permission for this operation")
            return False

    def check_metadata_validity(self, meta_data):
        return True


    def handle_text_to_image_request(self, request: ImageGenerationRequest) -> ImageGenerationResponse:
        op_valid=self.op_validity(request.operation)
        if not op_valid:
            ops = OperationStatus(success="false", error_code="", debug_log="", package_sent_time="", counter=12)
            images_data =""
        else:
            business_logic= TextToImageOperation(request)
            images_data=business_logic.response

            ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)
        return ImageGenerationResponse(operation=ops, data=images_data)


    def handle_source_monitoring_request(self):

        business_logic = SourceMonitoringOperation()
        return SourceMonitoringOperation.prepare_response_for_source_monitoring()



    # app_version: str = Field(alias="appVersion")

    def handle_report_bug_request(self, request: BugReportRequest) -> RegisterUser200Response:
        # app_version: str = Field(alias="appVersion")
        # installation_id: str = Field(alias="installationId")
        # timestamp: datetime = Field(alias="timestamp")
        # locale: str = Field(alias="locale")
        # platform: RegisterUserRequestPlatform = Field(alias="platform")

        # business_logic = RegisterOperation(request)
        # user_id = business_logic.user_id
        return ""

    def handle_register_user_request(self, request: RegisterUserRequest) -> RegisterUser200Response:
        # app_version: str = Field(alias="appVersion")
        # installation_id: str = Field(alias="installationId")
        # timestamp: datetime = Field(alias="timestamp")
        # locale: str = Field(alias="locale")
        # platform: RegisterUserRequestPlatform = Field(alias="platform")

            business_logic= RegisterOperation(request)
            user_id=business_logic.user_id
            return RegisterUser200Response(message="succesful", user_id=user_id)


    def handle_increase_user_limit_request(self, request: IncreaseUserLimitRequest) -> IncreaseUserLimit200Response:
        op_valid=self.op_validity(request.operation)
        if not op_valid:
            ops = OperationStatus(success="false", error_code="", debug_log="", package_sent_time="", counter=12)
        else:
            business_logic= IncreaseLimitOperation(request)
            success=business_logic.response
            if success:
                return IncreaseUserLimit200Response(message="succesful", newLimit=100)

    def handle_image_manipulation_request(self, request: MANDOMIMAGEPostRequest) -> DOMImageManipulationResponse:
        op_valid=self.op_validity(request.operation)
        if not op_valid:
            ops = OperationStatus(success="false", error_code="", debug_log="", package_sent_time="", counter=12)
            images_data =""
        else:
            business_logic= ImageManipulationOperation(request)
            images_data=business_logic.response

            ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)
        return ImageManipulationResponse(operation=ops, data=images_data)

    def handle_usr_image_manipulation_request(self, request: MANUSRIMAGEPostRequest) -> UserImageManipulationResponse:
        op_valid = self.op_validity(request.operation)
        if not op_valid:
            ops = OperationStatus(success="false", error_code="", debug_log="", package_sent_time="", counter=12)
            images_data = ""
        else:
            p = UsrImageManipulationOperation(request)
            data = p.response
            ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)
        return UserImageManipulationResponse(operation=ops, data=data)

    def handle_dom_image_manipulation_request(self, request: MANDOMIMAGEPostRequest) -> DOMImageManipulationResponse:
        op_valid=self.op_validity(request.operation)
        if not op_valid:
            ops = OperationStatus(success="false", error_code="", debug_log="", package_sent_time="", counter=12)
            images_data =""
        else:
            p=DomImageManipulationOperation(request)
            images_data=p.dom_response_data
            ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)
        return DOMImageManipulationResponse(operation=ops, data=images_data)




        #     self.DATA_IS_VALID, unpacked_data = unpack_mandomimage_post_request(mandomimage_post_request)
        #     if  self.DATA_IS_VALID:
        #         head, details = extract_head_from_unpacked_data(self.iie, unpacked_data, self.logger)
        #
        #
        # (self.DATA_IS_VALID, DETAILS), result, et \
        #     = digest_package_content_and_make_headswap(self.iie,
        #                                                self.ch,
        #                                                config,
        #                                                data,
        #                                                self.logger)

        # self.elapsed_time.update(et)
        # if self.DATA_IS_VALID:
        #
        #     data_dict = prepare_data_dict_MAN_DOM(result, et)
        #     now = datetime.now()
        #     now_formatted_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        #     meta_dict = prepare_meta_dict(success=True,
        #                                   error_code="",
        #                                   debug_log="",
        #                                   package_sent_time=now_formatted_time,
        #                                   extra_field=self.elapsed_time)
        #
        #     self.response = {
        #         "operation": meta_dict,
        #         "data": data_dict

            }

    #     else:
    #         data_dict = {}
    #
    #         if not DETAILS[0]:
    #             er = "img is not numpy array"
    #         elif not DETAILS[1]:
    #             er = "img doest have 3 channels "
    #         elif not DETAILS[2]:
    #             er = "img doesnt have a face"
    #         elif not DETAILS[3]:
    #             er = "img doesnt not have landmarks"
    #
    #         self.response = prepare_error_response(er, "")
    #
    # return self.response









    #
    # if not mandomimage_post_request.data:
    #     raise HTTPException(status_code=400, detail="Text for image generation is required")
    # # img = image_manipulation_request.data[0].image
    # data = mandomimage_post_request.data
    # config = mandomimage_post_request.config
    #
    # images_data = generate_cabinit_dom_img_man_data_response(data, config)
    # ## images_data = generate_image_data_response(img, txt, "")
    # ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)
    # #
    # return DOMImageManipulationResponse(operation=ops, data=images_data)
    def handle_MANIPULATE_USR_IMAGE(self, operation,config, data):

        self.logger.debug(" >>>handle_MANIPULATE_USR_IMAGE() ")

        self.encoded_img=  data["user_image"]
        self.userid=             operation["userid"]
        self.package_sent_time = operation["package_sent_time"]

        request_allowed=check_metadata_validity(operation)

        if not request_allowed:

            self.META_IS_VALID=False
            now = datetime.now()
            now_formatted_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

            meta_dict=prepare_meta_dict(success=False,
                              error_code="user_not_allowed" ,
                              debug_log= "",
                              package_sent_time= now_formatted_time ,
                              extra_field= "")

            data_dict= {}

            self.response= {
                  "operation":meta_dict,
                   "data":data_dict

            }

        else:
            (self.DATA_IS_VALID,DETAILS) ,source, et=digest_package_content_and_extract_head(self.iie, self.encoded_img, self.logger)
            if self.DATA_IS_VALID:

                data_dict=prepare_data_dict(source,et)

                now = datetime.now()
                now_formatted_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

                meta_dict = prepare_meta_dict(success=True,
                                              error_code="",
                                              debug_log="",
                                              package_sent_time=now_formatted_time,
                                              extra_field="")


                self.response = {
                    "operation": meta_dict,
                    "data": data_dict

                }



            else :
                data_dict ={}

                if not DETAILS[0]:
                    er=  "img is not numpy array"
                elif not DETAILS[1]:
                    er = "img doest have 3 channels "
                elif not DETAILS[2]:
                    er = "img doesnt have a face"
                elif not DETAILS[3]:
                    er = "img doesnt not have landmarks"

                now = datetime.now()
                now_formatted_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                meta_dict = prepare_meta_dict(success=False,
                                              error_code="data_not_valid",
                                              debug_log=er,
                                              package_sent_time=now_formatted_time,
                                              extra_field="")

                # print(" ")
                # print(" ")
                # print( self.response)
                self.response = {
                    "operation": meta_dict,
                    "data": data_dict

                }
                # self.response=prepare_post_answer_for_MANIPULATE_USR_IMAGE(  self.iie, self.encoded_img, self.logger)

        return self.response

    def handle_MANIPULATE_DOM_IMAGE(self, operation,config, data):
        logger = logging.getLogger("FelixRequestHandler")
        logger.setLevel(logging.DEBUG)

        request_allowed = check_metadata_validity(operation)

        if not request_allowed:
            self.META_IS_VALID = False
            error_message= "user_not_allowed"
            self.response=prepare_error_response(error_message, "")

        else:
            (self.DATA_IS_VALID, DETAILS), result,et\
                = digest_package_content_and_make_headswap(self.iie,
                                                           self.ch,
                                                           config,
                                                           data,
                                                         self.logger)


            # self.elapsed_time.update(et)
            if self.DATA_IS_VALID:

                data_dict = prepare_data_dict_MAN_DOM(result, et)
                now = datetime.now()
                now_formatted_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                meta_dict = prepare_meta_dict(success=True,
                                              error_code="",
                                              debug_log="",
                                              package_sent_time=now_formatted_time,
                                              extra_field=self.elapsed_time)

                self.response = {
                    "operation": meta_dict,
                    "data": data_dict

                }

            else:
                data_dict = {}

                if not DETAILS[0]:
                    er = "img is not numpy array"
                elif not DETAILS[1]:
                    er = "img doest have 3 channels "
                elif not DETAILS[2]:
                    er = "img doesnt have a face"
                elif not DETAILS[3]:
                    er = "img doesnt not have landmarks"


                self.response = prepare_error_response(er, "")

        return self.response


def prepare_error_meta_dict(error_message):
    now = datetime.now()
    now_formatted_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    meta_dict = prepare_meta_dict(success=False,
                                  error_code=error_message,
                                  debug_log="",
                                  package_sent_time=now_formatted_time ,
                                  extra_field="")
    return meta_dict


def prepare_error_response(error_message, debug):
    now = datetime.now()
    now_formatted_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    meta_dict = prepare_meta_dict(success=False,
                                  error_code=error_message,
                                  debug_log=debug,
                                  package_sent_time=now_formatted_time,
                                  extra_field="")
    data_dict = {}

    response = {
        "operation": meta_dict,
        "data": data_dict

    }
    return response


    # def check_compatibility(self):
    #     if self.fo.TARGET_IMG_HAS_3_CHANNEL:
    #         if self.fo.FACE_EXIST:
    #             if self.fo.LANDMARK_EXIST:
    #                 self.compatibility_code = 1
    #             else:
    #                 self.compatibility_code = -2
    #         else:
    #             self.compatibility_code = -1
    #     else:
    #         self.compatibility_code = 0


#
#
# class FelixInternetObj:
#     def __init__(self, url):
#         self.url = url
#         self.manipulated_image = False
#         self.manipulated_image_FLAG = False
#         self.LINK_IS_IMAGE = False
#         self.IMAGE_HAS_FACE = False
#         self.IMG_IS_COMPATIBLE = False
#         self.image = 0
#
#     def save_manipulatedimg_to_local(self, save_folder_path):
#         if self.IMG_IS_COMPATIBLE == True:
#             filename = create_random_name(8) + ".jpg"
#             self.filename = filename
#             full_save_path = save_folder_path + filename
#             self.full_save_path = full_save_path
#
#             cv2.imwrite(
#                 full_save_path, cv2.cvtColor(self.manipulated_image, cv2.COLOR_RGB2BGR)
#             )
#
#             # if self.manipulated_image:
#             #     cv2.imwrite(full_save_path, cv2.cvtColor(self.manipulated_image, cv2.COLOR_RGB2BGR) )
#
#     def upload_img_to_aws(self):
#         if self.IMG_IS_COMPATIBLE == True:
#             url = "https://s3-%s.amazonaws.com/%s/%s" % (
#                 location,
#                 bucket,
#                 self.filename,
#             )
#             self.manipulated_image_url = url
#             uploaded = upload_to_aws(s3, self.full_save_path, bucket, self.filename)
#
#     def create_felix_image_dict(self):
#         if self.IMG_IS_COMPATIBLE == False:
#             xurl = self.url
#
#         elif self.LINK_IS_IMAGE:
#             xurl = self.manipulated_image_url
#         else:
#             xurl = self.url
#
#         image_dict = {
#             "id": 0,
#             "src": self.url,
#             "left": 0,
#             "top": 0,
#             "manipulatedImage": xurl,
#         }
#
#         self.image_dict = image_dict
