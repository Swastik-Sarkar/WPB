import os
import tkinter

class rgbx():
    def bg(code): 
        return "\33[{code}m".format(code=code)

    def st(code): 
        return "\33[{code}m".format(code=code)   

    def ct(code): 
        return "\33[{code}m".format(code=code) 


app = Tk()
app.title("WPB - Windows Performance Booster")
app.geometry('1920x800')
appmenu = Menu(app)
item = Menu(appmenu)
item.add_command(label='update',fg='blue',command='item_update')
appmenu.add_cascade(label='App', appmenu=item)
app.config(appmenu = appmenu)
app.mainloop()

def item_update():
     os.system("start update")
