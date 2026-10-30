from tkinter import*
import tkinter as tk
import tkinter.messagebox
import random
number= random.randint(1,20)
def show_message():
    guessin= guess.get()
    g= int(guessin)
    if g>number:
        tkinter.messagebox.showinfo("high guess","your guess is too high")
    elif g<number:
        tkinter.messagebox.showinfo("low guess","your guess is too low")
    elif g==number:
        tkinter.messagebox.showinfo("correct guess","good job you guessed it!")
def confirm():
    my_name= name.get()
    tkinter.messagebox.showinfo("name","Hey"+ my_name +"I picked a number between 1-20 can you guess it?")

window= Tk()
window.title("Guess the number")
window.geometry("500x350")
title= Label(window,text="Welcome to the game!",font="Arial 20")
title.place(x=150,y=5)
l_name= Label(window,text="what is your name:")
l_name.place(x=50,y=100)
name= Entry(window)
name.place(x=170,y=100)
ok= Button(window,text="OK",command=confirm)
ok.place(x=310,y=95)
g_label= Label(window,text="Take a guess:")
g_label.place(x=50,y=200)
guess= Entry(window)
guess.place(x=170,y=200)
guess_b= Button(window,text="GUESS",command=show_message)
guess_b.place(x=310,y=195)


window.mainloop()