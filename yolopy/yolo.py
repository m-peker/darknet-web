from yolopy.pydarknet import Detector, Image as DarkNetImage
from PIL import Image
import cv2, os, numpy as np

class YoloNetwork():
    instance = None
    network = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if YoloNetwork.instance == None:
            YoloNetwork()

        return YoloNetwork.instance
   
    def __init__(self):
        """ Virtually private constructor. """
        if YoloNetwork.instance == None:
            YoloNetwork.instance = self
            self.network = self.create_network()

    def create_network(self):
        return Detector(
            bytes("yolopy/cfg/yolov3.cfg", encoding="utf-8"),
            bytes("yolopy/weights/yolov3.weights", encoding="utf-8"),
            0,
            bytes("yolopy/cfg/coco.data", encoding="utf-8")
        )

    def detect_objects(self, original_image):
        img = cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2BGR)
        img2 = DarkNetImage(img)

        return self.network.detect(img2)

    def get_tagged_image(self, original_image, results):
        for cat, _, bounds in results:
            x, y, w, h = bounds
            cv2.rectangle(original_image, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (255, 0, 0), thickness=2)
            cv2.putText(original_image,str(cat.decode("utf-8")),(int(x),int(y)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))

        return Image.fromarray(original_image)
