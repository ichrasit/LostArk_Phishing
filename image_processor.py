import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, isaret_path, bar_path):
        self.isaret_template = cv2.imread(isaret_path, 0)
        self.bar_template = cv2.imread(bar_path, 0)

    def isaret_bul(self, ekran_goruntusu):
        res = cv2.matchTemplate(ekran_goruntusu, self.isaret_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        return max_loc if max_val > 0.8 else None
    
    def bar_imlec_bul(self, ekran_goruntusu):
        res = cv2.matchTemplate(ekran_goruntusu, self.bar_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        return max_loc if max_val > 0.8 else None

    def turuncu_alani_bul(self, imlec_koordinatlari, config):
        x_koordinat = imlec_koordinatlari[0]
        return config["turuncu_alan_baslama"] <= x_koordinat <= config["turuncu_alan_bitis"]
    