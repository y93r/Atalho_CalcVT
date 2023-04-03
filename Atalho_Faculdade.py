#!/usr/bin/env python
# coding: utf-8

# In[3]:


#bibliotecas
import tkinter as tk
import os
from tkinter import filedialog
from os import path
import shutil
from tkinter.filedialog import askopenfilename


# Lista com os caminhos dos arquivos
files = [r'C:\Users\Usuário\Documents\Planej_2023.ods', 
         r'C:\Users\Usuário\Documents\Faculdade\Notas.ods'
         ]

def open_file(file_index):
    if os.path.exists(files[file_index]):
        os.startfile(files[file_index])
    else:
        tk.messagebox.showerror("Arquivo não encontrado!", ''' Verifique se o arquivo existe ou se foi renomeado''')
        
#diretorios completos para abrir um arquivo
def open_dir_faculdade():    
    folder_path = r'C:\Users\Usuário\Documents\Faculdade\ '
    if os.path.exists(folder_path):
        file1 = filedialog.askopenfilename(initialdir=path.dirname(folder_path))
        if file1:
            os.startfile(file1)
    else:
        tk.messagebox.showerror("Diretório não encontrado não encontrado!", ''' Verifique se o diretório existe ou se foi renomeado''')

#abrir Ava

def open_ava():
    import webbrowser
    
    url = "https://univirtus.uninter.com/ava/web/"
    webbrowser.open(url)
    
root = tk.Tk()
root.geometry("400x450")
root.title('Atalho para abrir arquivos')

# Botão para abrir Planejamento
button1 = tk.Button(root, text="Abrir Planejamento $", command=lambda: open_file(0), width=50)
button1.pack(pady=10)

# Botão para abrir Notas
button2 = tk.Button(root, text="Abrir Notas", command=lambda: open_file(1), width=50)
button2.pack(pady=10)

# Botão para abrir o diretório da faculdade
button3 = tk.Button(root, text="Abrir Diretório Faculdade", command=open_dir_faculdade, width=50)
button3.pack(pady=10)

# Botão para entrar no site da faculdade 
button3 = tk.Button(root, text="Abrir Ava", command=open_ava, width=50)
button3.pack(pady=10)

# Crédito
credit_label = tk.Label(root, text='Desenvolvido por Yara de Oliveira Rufino', font=('Arial', 10), fg='gray')
credit_label.pack(side='bottom', padx=10, pady=10)

root.mainloop()


# In[ ]:




