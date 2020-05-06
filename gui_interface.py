import tkinter as tk
from countries_most import country_most_tourists
from tourist_per_year import most_tourists
from transport_type import transport
from tourist_per_quarter import tourists_quarter


window = tk.Tk()

frame = tk.Frame(width = 900,
                 height = 600,
                 background = '#CACED8')

button1 = tk.Button(text='Tourists per year',
                    width = 30,
                    height = 10,
                    activeforeground = '#2DAF54',
                    bg = '#2DAF54',
                    command = lambda: most_tourists()
                    )

button2 = tk.Button(text='Countries with most tourists per year',
                    width = 30,
                    height = 10,
                    activeforeground = '#2DAF54',
                    bg = '#2DAF54',
                    command = lambda: country_most_tourists(1)
                    )

button3 = tk.Button(text='Type of transport',
                    width = 30,
                    height = 10,
                    activeforeground = '#2DAF54',
                    bg = '#2DAF54',
                    command = lambda: transport()
                    )

button4 = tk.Button(text='Tourists per quarter',
                    width = 30,
                    height = 10,
                    activeforeground = '#2DAF54',
                    bg = '#2DAF54',
                    command = lambda: tourists_quarter()
                    )


button1.place(x=40, y=40)
button2.place(x=40, y=400)
button3.place(x=640, y=40)
button4.place(x=640, y=400)


frame.grid()

window.mainloop()
