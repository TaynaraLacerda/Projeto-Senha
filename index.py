from tkinter import * 
from tkinter import messagebox
#Tela 1

cliente=Tk()
cliente.title("Solicitar Senha")
cliente.geometry("300x250")
cliente.configure(bg="lightgreen")

contador = 1
fila = []
senha_atual = StringVar()
senha_atual.set("---")

#Tela 2 

admin = Toplevel(cliente)
admin.title("Administrador")
admin.geometry("300x350")
admin.configure(bg="lightgreen")

# Lista da fila no admin

Label(admin, text="Fila de Senhas", font=("Arial",14)).pack(pady=10)

lista_admin = Listbox(admin, width=20, height=10)
lista_admin.pack(pady=10)

# Lista da fila no admin

Label(admin, text="Fil de Senhas", font=("Arial", 14)).pack(pady=10)

lista_admin = Listbox(admin, width=20, height=10)
lista_admin.pack(pady=10)

# Tela 3

painel = Toplevel(cliente)
painel.title("Painel de Senhas")
painel.geometry("400x300")
painel.configure(bg="lightgreen")

Label(painel, text="Senha Atual", font=("Arial", 20)).pack(pady=20)

Label (
    painel,
    textvariable=senha_atual,
    font=("Arial",40),
    fg="red"

).pack(pady=20)

cliente.mainloop()