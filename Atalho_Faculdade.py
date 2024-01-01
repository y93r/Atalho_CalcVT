#bibliotecas
import tkinter as tk
import os
from tkinter import filedialog
from os import path
import shutil
from tkinter.filedialog import askopenfilename
import subprocess
from datetime import datetime

ano_atual = str(datetime.now().year)

#Lista com os caminhos dos arquivos
files = [r'C:\Users\Documents\Planej_{}.xlsx'.format(ano_atual), 
         r'C:\Users\Documents\Faculdade\Notas.xlsx'
         ]

def open_file(file_index):
    if os.path.exists(files[file_index]):
        os.startfile(files[file_index])
    else:
        tk.messagebox.showerror("Arquivo não encontrado!", ''' Verifique se o arquivo existe ou se foi renomeado''')
        
#diretorios completos para abrir um arquivo
def open_dir_faculdade():    
    folder_path = r'C:\Users\Documents\Faculdade\ '
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
       
def open_dir_cursos():    
    folder_path = r'C:\Users\Documents\Cursos\ '
    if os.path.exists(folder_path):
        file1 = filedialog.askopenfilename(initialdir=path.dirname(folder_path))
        if file1:
            os.startfile(file1)
    else:
        tk.messagebox.showerror("Diretório não encontrado não encontrado!", ''' Verifique se o diretório existe ou se foi renomeado''')

def open_calc_vt():
     subprocess.Popen([r"C:\Workspace\Vt\output\vt_calendar.exe"])
        
def open_dir_workspace():    
    folder_path = r'C:\Workspace\ '
    if os.path.exists(folder_path):
        file1 = filedialog.askopenfilename(initialdir=path.dirname(folder_path))
        if file1:
            os.startfile(file1)
    else:
        tk.messagebox.showerror("Diretório não encontrado não encontrado!", ''' Verifique se o diretório existe ou se foi renomeado''')
        
root = tk.Tk()
root.geometry("400x450")
root.title('GERENCIADOR DE ARQUIVOS')
root.resizable(False, False)

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
button4 = tk.Button(root, text="Abrir Ava", command=open_ava, width=50)
button4.pack(pady=10)

# Botão para abrir o diretório dos cursos
button5 = tk.Button(root, text="Abrir Diretório Cursos", command=open_dir_cursos, width=50)
button5.pack(pady=10)

# Botão para abrir o calculadora do VT
button6 = tk.Button(root, text="Abrir Calculadora VT", command=open_calc_vt, width=50)
button6.pack(pady=10)

# Botão para abrir o Diretório Workspace
button7 = tk.Button(root, text="Abrir Diretório Workspace", command=open_dir_workspace, width=50)
button7.pack(pady=10)

# Crédito
credit_label = tk.Label(root, text='Desenvolvido por Yara de Oliveira Rufino', font=('Arial', 10), fg='gray')
credit_label.pack(side='bottom', padx=10, pady=10)

root.mainloop()
