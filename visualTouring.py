import tkinter as tk
import operaciones as mt
window = tk.Tk()
window.title("sintaxis")
window.geometry("500x500")
window.resizable(False, False)
window.config(bg="#D3C3C3")

# entrysvalue
exprecionR = tk.StringVar()
resultado = tk.StringVar()

# functions
def comprobar():
    valor = mt.touringMachine(exprecionR.get())    
    print(valor)
    if(valor==True):
        resultado.set("valida")
    else:
        resultado.set("invalida")

# labels
tk.Label(window,text="escribe la variable/asignacion",font=('Calibri', 14),background="#D3C3C3").place(x=160,y=50)
tk.Label(window,text="variable1 = 10",font=('Calibri', 14),background="#D3C3C3").place(x=200,y=100)
tk.Label(window,text="la entrada debe estar formateada",font=('Calibri', 14),background="#D3C3C3").place(x=140,y=150)
tk.Label(window,textvariable=resultado,font=('Calibri', 14),background="#D3C3C3").place(x=200,y=390)

# entrys
tk.Entry(window,width=47,textvariable=exprecionR,font=('Calibri', 14)).place(x=10,y=200)


# buton
tk.Button(window,font=('Calibri', 14),text="comprobar",command=comprobar).place(x=200,y=430)

window.mainloop()