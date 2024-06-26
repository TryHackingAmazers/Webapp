import sys
sys.path.append('./recommendation')
sys.path.append('./device_finder')

from device_finder.find_objects import parse_image,compare
from device_finder.image_ui import preprocess
from recommendation.appliance_selector import get_recommendations
from recommendation.object_recommender import choose_object
import recommendation.yolov_model as ym

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

def preprocess_image(image_path):
    path = generate_random_filename('jpg')
    return preprocess(image_path,path),path

def find_on_amazon(image_path,id):
    return compare(image_path,id)

# print(find_on_amazon('/home/rohan/hackonama/sample_images/TimberlandkingLSWENGE_0d80ca15-a0ad-4341-8b5e-4efa70f4c7a5.webp',0))
