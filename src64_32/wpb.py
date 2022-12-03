import os
import tkinter as tk
import pyglet
from tkextrafont import Font

pyglet.font.add_file('tklabelfont.ttf')

class rgbx():
    def bg(code): 
        return "\33[{code}m".format(code=code)

    def st(code): 
        return "\33[{code}m".format(code=code)   

    def ct(code): 
        return "\33[{code}m".format(code=code) 


app = Tk()
applabelfont = Font(file="text_deafault.ttf", family="text_deafult")
app.title("WPB - Windows Performance Booster")
app.geometry('1920x800')
appmenu = Menu(app)
item = Menu(appmenu)
item.add_command(label='update',fg='blue',command='item_update')
appmenu.add_cascade(label='App', appmenu=item)
app.config(appmenu = appmenu)
tk.Label(app, text="WPB", font=font).pack()
app.mainloop()

def item_update():
     os.system("start update")
