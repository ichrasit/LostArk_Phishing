import cv2
import pyautogui
import numpy as np
import time
from config import CONFIG
from image_processor import ImageProcessor
from action_handler import ActionHandler

def main():
    image_processor = ImageProcessor("assets/isaret.png", "assests/bar.png")
    action_handler = ActionHandler(CONFIG)

    while True:
        ekran_goruntusu = np.array(pyautogui.screenshot())
        gri_goruntu = cv2.cvtColor(ekran_goruntusu, cv2.COLOR_BGR2GRAY)

        isaret_koordinat = image_processor.isaret_bul(gri_goruntu)
        action_handler.balik_cek(isaret_koordinat)

        imlec_koordinatlari = image_processor.bar_imlec_bul(gri_goruntu)
        turuncu_alanda_mi = image_processor.turuncu_alani_bul(imlec_koordinatlari, CONFIG)
        action_handler.bar_takip(imlec_koordinatlari, turuncu_alanda_mi)

        if isaret_koordinat:
            action_handler.olta_at()

        time.sleep(CONFIG["kontrol_frekansi"])

if __name__ == "__main__":
    main()