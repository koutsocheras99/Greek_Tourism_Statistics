from tkinter import *
import tkinter as tk
from country_v3 import country_most_tourists
from tourist_per_year import most_tourists
from transport_type import transport
from tourist_per_quarter import tourists_quarter

def create_year_frame1():
    new_window = tk.Toplevel(window, width=450, height=300, background = '#CACED8')    
    Start_Scale = Scale(new_window, bd =5, label='Start Year', from_=2011, to=2015)
    Start_Scale.place(x=50, y=60)
    End_Scale = Scale(new_window, bd =5, label='End Year', from_=2011, to=2015)
    End_Scale.place(x=285, y=60)
    Confirmation_Button = tk.Button(new_window, text='Get Graph', bd=5, width = 10, height = 3, bg = '#2DAF54', command = lambda: most_tourists(start_year=Start_Scale.get(), end_year=End_Scale.get()))                    
    Confirmation_Button.place(x=190, y=195)

def create_year_frame2():
    new_window2 = tk.Toplevel(window, width=450, height=300, background = '#CACED8')    
    Start_Scale = Scale(new_window2, bd =5, label='Start Year', from_=2011, to=2015)
    Start_Scale.place(x=50, y=60)
    End_Scale = Scale(new_window2, bd =5, label='End Year', from_=2011, to=2015)
    End_Scale.place(x=285, y=60)
    Confirmation_Button = tk.Button(new_window2, text='Get Graph', bd=5, width = 10, height = 3, bg = '#2DAF54', command = lambda: country_most_tourists((8), start_year=Start_Scale.get(), end_year=End_Scale.get())) 
    Confirmation_Button.place(x=190, y=195)

def create_year_frame3():
    new_window3 = tk.Toplevel(window, width=450, height=300, background = '#CACED8')    
    Start_Scale = Scale(new_window3, bd =5, label='Start Year', from_=2011, to=2015)
    Start_Scale.place(x=50, y=60)
    End_Scale = Scale(new_window3, bd =5, label='End Year', from_=2011, to=2015)
    End_Scale.place(x=285, y=60)
    Confirmation_Button = tk.Button(new_window3, text='Get Graph', bd=5, width = 10, height = 3, bg = '#2DAF54', command = lambda: transport(start_year=Start_Scale.get(), end_year=End_Scale.get()))                    
    Confirmation_Button.place(x=190, y=195)

def create_year_frame4():
    new_window4 = tk.Toplevel(window, width=450, height=300, background = '#CACED8')    
    Start_Scale = Scale(new_window4, bd =5, label='Start Year', from_=2011, to=2015)
    Start_Scale.place(x=50, y=60)
    End_Scale = Scale(new_window4, bd =5, label='End Year', from_=2011, to=2015)
    End_Scale.place(x=285, y=60)
    Confirmation_Button = tk.Button(new_window4, text='Get Graph', bd=5, width = 10, height = 3, bg = '#2DAF54', command = lambda: tourists_quarter(start_year=Start_Scale.get(), end_year=End_Scale.get()))                    
    Confirmation_Button.place(x=190, y=195)

window = tk.Tk()

frame = tk.Frame(width = 900,
                 height = 600,
                 background = '#CACED8')

button1 = tk.Button(text='Tourists per year',
                    width = 30,
                    height = 10,
                    activeforeground = '#2DAF54',
                    bg = '#2DAF54',
                    command = create_year_frame1
                    )

button2 = tk.Button(text='Countries with most tourists per year',
                    width = 30,
                    height = 10,
                    activeforeground = '#2DAF54',
                    bg = '#2DAF54',
                    command = create_year_frame2
                    )

button3 = tk.Button(text='Type of transport',
                    width = 30,
                    height = 10,
                    activeforeground = '#2DAF54',
                    bg = '#2DAF54',
                    command = create_year_frame3
                    )

button4 = tk.Button(text='Tourists per quarter',
                    width = 30,
                    height = 10,
                    activeforeground = '#2DAF54',
                    bg = '#2DAF54',
                    command = create_year_frame4
                    )



button1.place(x=40, y=40)
button2.place(x=40, y=400)
button3.place(x=640, y=40)
button4.place(x=640, y=400)


frame.grid()

window.mainloop()
