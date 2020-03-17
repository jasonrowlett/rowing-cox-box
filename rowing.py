##################################################################
##################################################################
'''MAIN FILE FOR RASPBERRY PI USB'''
'''combines the custom modules with frontend design'''
##################################################################
##################################################################

from tkinter import *
import tkinter as tk
from tkinter.ttk import *
#from modules import stopWatch as stw
# import GPIO

root = Tk()
root.geometry('800x480')

style = Style()

# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).

'''LAYOUT'''

root = tk.Tk()

w = tk.Label(root, bg="#0000cc")
w.pack(fill=tk.X)

tk.mainloop()



'''BUTTONS'''

style.configure('W.TButton', font =
               ('tahoma', 18),
                foreground = 'black',
                background = 'white')

# Style will be reflected only on
# this button because we are providing
# style only on this Button.
''' Button 1'''
btn1 = Button(root, text = 'Start/Pause', style = 'W.TButton', command = None)
btn1.grid(row = 50, column = 1, pady = 375, padx = 30)

''' Button 2'''
btn2 = Button(root, text = 'Finish', style = 'W.TButton', command = None)
btn2.grid(row = 50, column = 2, pady = 375, padx = 30)


'''STOPWATCH'''
#StopWatch Module imported

style.configure('W.TBox', font = 'tahoma', size=18,
                foreground = 'black',
                background = 'white')

def block():
    block1 = block(root, text = '00:00:00', style = 'W.TButton', command = None)
    block1.grid(row = 40, column = 1, pady = 350, padx = 25)






'''MAP'''




root.mainloop()
