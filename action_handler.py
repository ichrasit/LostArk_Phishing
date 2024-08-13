import pyautogui
import time

class ActionHandler:
    def __init__(self, config):
        self.config = config
    
    def bas(self, key):
        pyautogui.press(key)
    
    def olta_at(self):
        self.bas(self.config["olta_tusu"])
    
    def balik_cek(self, isaret_koordinat):
        if isaret_koordinat:
            self.olta_at()
    
    def bar_takip(self, imlec_koordinatlari, turuncu_alanda_mi):
        if turuncu_alanda_mi:
            self.bas(self.config["bar_tusu"])
