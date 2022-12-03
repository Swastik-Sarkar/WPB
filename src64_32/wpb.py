import os

os.system("title windows performance booster")
class rgbx():
    def bg(code): 
        return "\33[{code}m".format(code=code)

    def st(code): 
        return "\33[{code}m".format(code=code)   

    def ct(code): 
        return "\33[{code}m".format(code=code) 

wbp_logo = rgbx.bg(97) + rgbx.st(4) + ct(1) + "WBP"
