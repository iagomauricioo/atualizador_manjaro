import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def atualizar():
    root.destroy()
    comando = 'xterm -e "yay -Syyuu --noconfirm && sudo pacman -Syyuu --noconfirm; echo Pressione Enter para sair; read"'
    processo = subprocess.run(comando, shell=True)
    perguntar_reinicio()

def perguntar_reinicio():
    resposta = messagebox.askyesno("Reiniciar?", "Deseja rodar novamente o atualizador?")
    if resposta:
        reiniciar_script()
    else:
        sys.exit()

def reiniciar_script():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def sair():
    root.destroy()

root = tk.Tk()
root.title("Atualização do Sistema")
root.geometry("300x150")
root.eval('tk::PlaceWindow . center')

label = tk.Label(root, text="Quer atualizar o sistema?", font=("Arial", 12))
label.pack(pady=20)

botoes = tk.Frame(root)
botoes.pack()

btn_sim = tk.Button(botoes, text="Sim", width=10, command=atualizar)
btn_sim.grid(row=0, column=0, padx=10)

btn_nao = tk.Button(botoes, text="Não", width=10, command=sair)
btn_nao.grid(row=0, column=1, padx=10)

root.mainloop()
