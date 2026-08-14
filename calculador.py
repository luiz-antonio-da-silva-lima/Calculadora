import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
igual2x = False
def addBuffer(n):
    if n in ['+','-','*','/']:
        operador = n
    global igual2x       
    global Buffer
    global adicionado
    if igual2x == True and n not in ['+','-','*','/']:
        adicionado = n
        Buffer = f"{Buffer}{operador}{n}"
        igual2x = False
        atualizarBuffer()
    elif igual2x == False:
        adicionado = n
        Buffer = f"{Buffer}{n}"
        igual2x = False
        atualizarBuffer()

def BotaoIgual():
    global Buffer
    global adicionado
    global igual2x
    if igual2x == False:
            calcBuffer = f"{(eval(Buffer)):.2f}"
            Buffer = calcBuffer
            igual2x = True
            atualizarBuffer()
    elif igual2x == True:
            addBuffer(adicionado)

def atualizarBuffer():
    var.set(Buffer)

def LimparBuffer():
    global igual2x
    global Buffer
    Buffer = ""
    igual2x = False
    atualizarBuffer()

def criarGrid(frm):
    # Botões Numericos
    tk.Button(frm, text="1", font=("Arial", 14), width=10, command=lambda: addBuffer(1)).grid(column=1, row=1)
    tk.Button(frm, text="2", font=("Arial", 14), width=10, command=lambda: addBuffer(2)).grid(column=2, row=1)
    tk.Button(frm, text="3", font=("Arial", 14), width=10, command=lambda: addBuffer(3)).grid(column=3, row=1)
    tk.Button(frm, text="4", font=("Arial", 14), width=10, command=lambda: addBuffer(4)).grid(column=1, row=2)
    tk.Button(frm, text="5", font=("Arial", 14), width=10, command=lambda: addBuffer(5)).grid(column=2, row=2)
    tk.Button(frm, text="6", font=("Arial", 14), width=10, command=lambda: addBuffer(6)).grid(column=3, row=2)
    tk.Button(frm, text="7", font=("Arial", 14), width=10, command=lambda: addBuffer(7)).grid(column=1, row=3)
    tk.Button(frm, text="8", font=("Arial", 14), width=10, command=lambda: addBuffer(8)).grid(column=2, row=3)
    tk.Button(frm, text="9", font=("Arial", 14), width=10, command=lambda: addBuffer(9)).grid(column=3, row=3)
    tk.Button(frm, text="0", font=("Arial", 14), width=10, command=lambda: addBuffer(0)).grid(column=2, row=4)
    
    # Operadores
    tk.Button(frm, text="+", font=("Arial", 14), width=10, command=lambda: addBuffer('+')).grid(column=4, row=1)
    tk.Button(frm, text="-", font=("Arial", 14), width=10, command=lambda: addBuffer('-')).grid(column=4, row=2)
    tk.Button(frm, text="*", font=("Arial", 14), width=10, command=lambda: addBuffer('*')).grid(column=4, row=3)
    tk.Button(frm, text="/", font=("Arial", 14), width=10, command=lambda: addBuffer('/')).grid(column=4, row=4)
    
    # Ação
    tk.Button(frm, text="=", font=("Arial", 14), width=10, command=BotaoIgual).grid(column=4, row=5)
    tk.Button(frm, text="Apagar", font=("Arial", 14), width=10, command=LimparBuffer).grid(column=5, row=1)

def main():
    root = tk.Tk()
    root.title("Calculadora")
    
    global Buffer, var
    Buffer = ""
    var = tk.StringVar()
    var.set("")
    
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    
    label = tk.Label(frm, textvariable=var, font=("Arial", 14), anchor="e", width=27, relief="sunken", bd=1)
    label.grid(column=1, row=0, columnspan=5, pady=5, sticky="we")
    
    criarGrid(frm)
    root.mainloop()

if __name__ == "__main__":
    main()
