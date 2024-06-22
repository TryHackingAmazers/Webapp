import sys
sys.path.append('./recommendation')
sys.path.append('./device_finder')

from device_finder.find_objects import parse_image,compare
from recommendation.appliance_selector import get_recommendations
from recommendation.object_recommender import choose_object
import yolov_model as ym

import cv2
import numpy as np
import uuid

def generate_random_filename(extension):
    return str(uuid.uuid4()) + '.' + extension

def temp_save(input_image,path):
    input_image = cv2.imdecode(np.fromstring(input_image.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    cv2.imwrite(path,input_image)

def get_recommendation_objects(input_image,path):
    temp_save(input_image,path)
    score = ym.process_image(path)
    reco = get_recommendations(score)
    return reco

def get_similar_objects(item,path):
    return choose_object(item.lower(),path)
