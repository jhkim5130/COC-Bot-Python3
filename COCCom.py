import numpy as np
from PIL import ImageGrab
import cv2
import time
import pytesseract
import win32api, win32con
import PIL.ImageOps

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
class COCCom:
    state = 'home'
    
    def __init__(self):
        pass

    def search(self):
        if self.state != 'home':
            return None
        else:
            click(60,450)
            time.sleep(1)
            click(190,400)
            time.sleep(5)
            self.state = 'searched'

    def re_search(self):
        if self.state != 'searched':
            return  None
        else:
            click(750,375)
            time.sleep(10)
            
    def check_gold(self):
        if self.state != 'searched':
            return None
        else:
            check_gold = ImageGrab.grab(bbox=(48,105,110,120))
            check_gold_g = check_gold.convert('L')
            inverted_image = PIL.ImageOps.invert(check_gold_g)
            parsed = pytesseract.image_to_string( inverted_image, config='--psm 7 digits').\
                        replace(' ', '').replace('O', '0').replace('A', '4').replace('S', '5')
            print("before", parsed)
            parsed = int(''.join(filter(lambda x: '0'<=x<='9', parsed)))
            print("after", parsed)
            return parsed

    def attack(self):
        if self.state != 'searched':
            return None
        else:
            N = 115
            unit_potrait_pos = [(100, 450),
                                (160, 450)]
            edges = [((570, 410), (800, 240)),
                     ((750, 200), (560, 55)),
                     ((250, 55), (80, 200)),
                     ((60, 285), (170, 360)),]
            for k in range(2):               
                for ux, uy in unit_potrait_pos:
                    click(ux,uy)
                    for p1, p2 in edges:
                        for j in range(int(N/len(edges))):
                            x, y = tuple(int(p1[i]+j*(p2[i]-p1[i])/int(N/len(edges))) for i in (0,1))
                            click(x,y)
                            time.sleep(0.05)
                        
    def get_state(self):
        return self.state
    
    
    