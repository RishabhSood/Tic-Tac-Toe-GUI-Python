# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 18:01:04 2019

@author: soodr
"""

import tkinter
from tkinter import Button
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import messagebox
import time


def myGame():
    window = tkinter.Tk()
    
    window.title("Tic Tac Toe Mania")
    window.geometry("500x340")
    
    lbl = Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'), padx = 10, pady = 10)
    lbl.grid(row=1,column=1)
    
    ply1 = StringVar()
    ply2 = StringVar()
    pl1_name = StringVar()
    pl2_name = StringVar()
    
    lb1 = Label(window, text="Player 1 Name: ")
    lb1.grid(row=2,column=2)
    
    pl1_entry = Entry(window, textvariable=pl1_name)
    pl1_entry.grid(row=2,column=3, columnspan = 3)
    
    lbl1 = Label(window, text="Player 1 Choice: ")
    lbl1.grid(row=2,column=0)
    
    ply1_entry = Entry(window, textvariable=ply1)
    ply1_entry.grid(row=2,column=1, columnspan = 3)
    
    lb2 = Label(window, text="Player 2 Name: ")
    lb2.grid(row=3,column=2)
    
    pl2_entry = Entry(window, textvariable=pl2_name)
    pl2_entry.grid(row=3,column=3, columnspan = 3)
    
    lbl2 = Label(window, text="Player 2 Choice: ")
    lbl2.grid(row=3,column=0)
    
    ply2_entry = Entry(window, textvariable=ply2)
    ply2_entry.grid(row=3,column=1, columnspan = 3)
    
    turn = 1; 
    
    def clicked1():
        global turn
        p1 = ply1.get()
        p2 = ply2.get()
        
        if p1 == "" or p2 == "":
            error = Label(window, text="Invalid Field Entry/Entries!!")
            error.grid(row=10,column=1)
            time.sleep(3)
            window.destroy()
        
        if btn1["text"]==" ":
            if turn==1:
                turn=2;
                btn1["text"]=p1
            elif turn==2:
                turn=1;
                btn1["text"]=p2
            check();
    def clicked2():
        global turn
        p1 = ply1.get()
        p2 = ply2.get()
        
        if p1 == "" or p2 == "":
            error = Label(window, text="Invalid Field Entry/Entries!!")
            error.grid(row=10,column=1)
            time.sleep(3)
            window.destroy()
            
        if btn2["text"]==" ":
            if turn==1:
                turn=2;
                btn2["text"]=p1
            elif turn==2:
                turn=1;
                btn2["text"]=p2
            check();
    def clicked3():
        global turn
        p1 = ply1.get()
        p2 = ply2.get()
        
        if p1 == "" or p2 == "":
            error = Label(window, text="Invalid Field Entry/Entries!!")
            error.grid(row=10,column=1)
            time.sleep(3)
            window.destroy()
            
        if btn3["text"]==" ":
            if turn==1:
                turn=2;
                btn3["text"]=p1
            elif turn==2:
                turn=1;
                btn3["text"]=p2
            check();
    def clicked4():
        global turn
        p1 = ply1.get()
        p2 = ply2.get()
        
        if p1 == "" or p2 == "":
            error = Label(window, text="Invalid Field Entry/Entries!!")
            error.grid(row=10,column=1)
            time.sleep(3)
            window.destroy()
            
        if btn4["text"]==" ":
            if turn==1:
                turn=2;
                btn4["text"]=p1
            elif turn==2:
                turn=1;
                btn4["text"]=p2
            check();
    def clicked5():
        global turn
        p1 = ply1.get()
        p2 = ply2.get()
        
        if p1 == "" or p2 == "":
            error = Label(window, text="Invalid Field Entry/Entries!!")
            error.grid(row=10,column=1)
            time.sleep(3)
            window.destroy()
            
        if btn5["text"]==" ":
            if turn==1:
                turn=2;
                btn5["text"]=p1
            elif turn==2:
                turn=1;
                btn5["text"]=p2
            check();
    def clicked6():
        global turn
        p1 = ply1.get()
        p2 = ply2.get()
        
        if p1 == "" or p2 == "":
            error = Label(window, text="Invalid Field Entry/Entries!!")
            error.grid(row=10,column=1)
            time.sleep(3)
            window.destroy()
            
        if btn6["text"]==" ":
            if turn==1:
                turn=2;
                btn6["text"]=p1
            elif turn==2:
                turn=1;
                btn6["text"]=p2
            check();
    def clicked7():
        global turn
        p1 = ply1.get()
        p2 = ply2.get()
        
        if p1 == "" or p2 == "":
            error = Label(window, text="Invalid Field Entry/Entries!!")
            error.grid(row=10,column=1)
            time.sleep(3)
            window.destroy()
            
        if btn7["text"]==" ":
            if turn==1:
                turn=2;
                btn7["text"]=p1
            elif turn==2:
                turn=1;
                btn7["text"]=p2
            check();
    def clicked8():
        global turn
        p1 = ply1.get()
        p2 = ply2.get()
        
        if p1 == "" or p2 == "":
            error = Label(window, text="Invalid Field Entry/Entries!!")
            error.grid(row=10,column=1)
            time.sleep(3)
            window.destroy()
            
        if btn8["text"]==" ":
            if turn==1:
                turn=2;
                btn8["text"]=p1
            elif turn==2:
                turn=1;
                btn8["text"]=p2
            check();
    def clicked9():
        global turn
        p1 = ply1.get()
        p2 = ply2.get()
        
        if p1 == "" or p2 == "":
            error = Label(window, text="Invalid Field Entry/Entries!!")
            error.grid(row=10,column=1)
            time.sleep(3)
            window.destroy()
            
        if btn9["text"]==" ":
            if turn==1:
                turn=2;
                btn9["text"]=p1
            elif turn==2:
                turn=1;
                btn9["text"]=p2
            check();
    
    flag=1;
    
    def check():
        global flag;
        b1 = btn1["text"];
        b2 = btn2["text"];
        b3 = btn3["text"];
        b4 = btn4["text"];
        b5 = btn5["text"];
        b6 = btn6["text"];
        b7 = btn7["text"];
        b8 = btn8["text"];
        b9 = btn9["text"];
        flag=flag+1;
        if b1==b2 and b1==b3 and b1==ply1.get() or b1==b2 and b1==b3 and b1==ply2.get():
            win(btn1["text"])
        if b4==b5 and b4==b6 and b4==ply1.get() or b4==b5 and b4==b6 and b4==ply2.get():
            win(btn4["text"]);
        if b7==b8 and b7==b9 and b7==ply1.get() or b7==b8 and b7==b9 and b7==ply2.get():
            win(btn7["text"]);
        if b1==b4 and b1==b7 and b1==ply1.get() or b1==b4 and b1==b7 and b1==ply2.get():
            win(btn1["text"]);
        if b2==b5 and b2==b8 and b2==ply1.get() or b2==b5 and b2==b8 and b2==ply2.get():
            win(btn2["text"]);
        if b3==b6 and b3==b9 and b3==ply1.get() or b3==b6 and b3==b9 and b3==ply2.get():
            win(btn3["text"]);
        if b1==b5 and b1==b9 and b1==ply1.get() or b1==b5 and b1==b9 and b1==ply2.get():
            win(btn1["text"]);
        if b7==b5 and b7==b3 and b7==ply1.get() or b7==b5 and b7==b3 and b7==ply2.get():
            win(btn7["text"]);
        if flag ==10:
            messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
            window.destroy()
    
    def win(player):
        if player == ply1.get():
            player = pl1_name.get()
        if player == ply2.get():
            player = pl2_name.get()
        ans = "Game complete " +player + " wins ";
        messagebox.showinfo("Congratulations", ans)
        newGame = messagebox.askquestion("New Game", "Do you wish to start a new game?")
        if newGame == 'yes':
            window.destroy()
            myGame()
        else:
            window.destroy()
    
    k = 50
    
    btn1 = Button(window, text=" ",bg="Black", fg="White",width=3,height=1,font=('Helvetica','20'),command=clicked1)
    btn1.place(x=50+k, y=120)
    btn2 = Button(window, text=" ",bg="Black", fg="White",width=3,height=1,font=('Helvetica','20'),command=clicked2)
    btn2.place(x=110+k, y=120)
    btn3 = Button(window, text=" ",bg="Black", fg="White",width=3,height=1,font=('Helvetica','20'),command=clicked3)
    btn3.place(x=170+k, y=120)
    btn4 = Button(window, text=" ",bg="Black", fg="White",width=3,height=1,font=('Helvetica','20'),command=clicked4)
    btn4.place(x=50+k, y=180)
    btn5 = Button(window, text=" ",bg="Black", fg="White",width=3,height=1,font=('Helvetica','20'),command=clicked5)
    btn5.place(x=110+k, y=180)
    btn6 = Button(window, text=" ",bg="Black", fg="White",width=3,height=1,font=('Helvetica','20'),command=clicked6)
    btn6.place(x=170+k, y=180)
    btn7 = Button(window, text=" ",bg="Black", fg="White",width=3,height=1,font=('Helvetica','20'),command=clicked7)
    btn7.place(x=50+k, y=240)
    btn8 = Button(window, text=" ",bg="Black", fg="White",width=3,height=1,font=('Helvetica','20'),command=clicked8)
    btn8.place(x=110+k, y=240)
    btn9 = Button(window, text=" ",bg="Black", fg="White",width=3,height=1,font=('Helvetica','20'),command=clicked9)
    btn9.place(x=170+k, y=240)
    
    window.mainloop()

myGame()