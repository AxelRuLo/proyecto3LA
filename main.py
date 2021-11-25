import tkinter as tk
from tkinter import font
from tkinter.constants import BOTTOM, END
from tkinter import filedialog
from unicodedata import normalize 

window = tk.Tk()
window.title("sintaxis")
window.geometry("800x700")
window.resizable(False, False)
window.config(bg="#F5F7BF")
data = 0
display_text = tk.StringVar()

# entrysvalue
exprecionR = tk.StringVar()
cadena = tk.StringVar()
resultado = tk.StringVar()




# labels
tk.Label(window,text="Analizador de sintaxis javaScript",font=('Calibri', 14),background="#F5F7BF").place(x=270,y=50)
tk.Label(window,text="selecciona el codigo js a revisar",font=('Calibri', 14),background="#F5F7BF").place(x=280,y=100)
tk.Label(window,textvariable=resultado,font=('Calibri', 14),background="#F5F7BF").place(x=200,y=390)

# entrys
textExample = tk.Label(window,height=14,textvariable=display_text,width=70,font=('Calibri',14),borderwidth=2, relief="solid").place(x=40,y=280)
# functions
def abrirTxt():
    global data
    documento = filedialog.askopenfilename(
    initialdir="C:/Users/MainFrame/Desktop/", 
    title="Open Text file", 
    filetypes=(("Text Files", ".js"),)
    )
    f = open(documento, "r",encoding="utf-8")
    data = f.readlines()
    print(data)

def comprobar():
    if(data == 0):
        display_text.set("no hay nada selecionado")
    else:
        display_text.set("analizando")





# buton
tk.Button(window,font=('Calibri', 14),text="seleccionar",command=abrirTxt,).place(x=350,y=150)
tk.Button(window,font=('Calibri', 14),text="comprobar",command=comprobar,).place(x=350,y=200)



window.mainloop()