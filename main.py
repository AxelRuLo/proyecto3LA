import tkinter as tk
from tkinter.constants import BOTTOM, END
window = tk.Tk()
window.title("sintaxis")
window.geometry("800x700")
window.resizable(False, False)
window.config(bg="#F5F7BF")

# entrysvalue
exprecionR = tk.StringVar()
cadena = tk.StringVar()
resultado = tk.StringVar()




# labels
tk.Label(window,text="Analizador de sintaxis javaScript",font=('Calibri', 14),background="#F5F7BF").place(x=270,y=50)
tk.Label(window,text="escribe el codigo js a revisar",font=('Calibri', 14),background="#F5F7BF").place(x=280,y=100)
tk.Label(window,textvariable=resultado,font=('Calibri', 14),background="#F5F7BF").place(x=200,y=390)

# entrys
textExample = tk.Text(window,height=30,width=90,)

# functions

def comprobar():
    result=textExample.get("1.0","end").splitlines()
    print(result)

textExample=tk.Text(window, height=30,width=90)
textExample.pack(side = BOTTOM)



# buton
tk.Button(window,font=('Calibri', 14),text="comprobar",command=comprobar,).place(x=350,y=150)



window.mainloop()