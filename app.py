import os
#Import the required Libraries
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("350x250")

#Define a function to update the entry widget
def entry_update(text):
   entry.delete(0,END)
   entry.insert(0,text)


#Create Multiple Buttons with different commands
button_dict={}
option= ["Tic Tac Toe", "Quiz Game", "Memory Puzzle Game", "Bubble Shooter"]
funcs = [lambda: os.system("python tic_tac_toe.py"), lambda: os.system("python quizgame.py"), lambda: os.system("python memorypuzzlegame.py"), lambda: os.system("python bubbleshooter.py")]

idx = 0

for i in option:
    button_dict[i]=ttk.Button(win, text=i, command= funcs[idx])
    button_dict[i].pack()
    idx += 1

win.mainloop()