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
            check_gold = ImageGrab.grab(bbox=(45,130,110,145))
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
    
    def end_attack(self):
        if self.state != 'seaeched':
            return None
        else:
            click(70,390)
            time.sleep(1)
            click(510,350)
            self.state = 'home'
        
    def make_unit(self):
        if self.state != 'home':
            return None
        else:
            click(40,380)
            time.sleep(1)
            click(540,170)
            time.sleep(1)
            click(735,569)
            time.sleep(1)
            click(780,170)
        
    def check_hole(self):
        img = np.array(ImageGrab.grab(bbox=(0,0,830,540)))
        template = cv2.imread('template3.jpg',0)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        print (min_val)
        
        if min_val < 5300000:
            return True
        else: return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        