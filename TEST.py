import COCCom

com = COCCom.COCCom()

com.search()


while com.check_gold() < 200000:
    com.re_search()

com.attack()