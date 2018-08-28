import COCCom
import time

com = COCCom.COCCom()


try:
    while True:
        print (com.get_state())           
        com.search()
        
        print (com.get_state())          
        while (com.check_gold() < 200000) and (com.check_hole() == True):
            print (com.get_state())          
            com.re_search()        
        
        print (com.get_state())          
        com.attack()        
        time.sleep(20)        
        
        print (com.get_state())          
        com.end_attack()
        
        print (com.get_state())          
        com.make_unit()
        time.sleep(1620)
except KeyboardInterrupt:
    pass