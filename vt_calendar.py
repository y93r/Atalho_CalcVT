#!/usr/bin/env python
# coding: utf-8

# In[4]:


from datetime import datetime, timedelta
from workadays import workdays as wd
import tkinter as tk
from tkcalendar import DateEntry
import babel.numbers

janela = tk.Tk()
janela.geometry("300x255")
janela.title('Calculadora de VT')

def calcular_vt():
    try:
        data_inicio = entry1.get_date()
        data_fim = entry2.get_date()
        if data_inicio > data_fim:
            result_label.config(text="A data de início deve ser anterior à data de término")
            return
        vt = float(entry3.get().replace(",", "."))
    except ValueError:
        result_label.config(text="Por favor, insira um valor válido para o Vale Transporte")
        return
    
    dias_trabalhado = wd.networkdays(data_inicio, data_fim, country='BR', state='SP')
    total_vt = vt * dias_trabalhado
    result = f"Total de dias trabalhados no período: {dias_trabalhado}\nTotal do vale transporte: R$ {total_vt:.2f}"
    result_label.config(text=result)

label_explicacao = tk.Label(text = "Selecione um período para a verificação", font=("Arial", 10, "bold"))
label_explicacao.pack()   
    
#data de inicio e final do período a ser calculado
label1 = tk.Label(text="Data de início:")
label1.pack()
entry1 = DateEntry(janela, width=20, date_pattern='dd/mm/yyyy', locale='pt_BR')
entry1.pack()

label2 = tk.Label(text="Data de término:")
label2.pack()
entry2 = DateEntry(janela, width=20, date_pattern='dd/mm/yyyy', locale='pt_BR')
entry2.pack()

#valor do vale transporte
label3 = tk.Label(text="Valor do Vale Transporte R$:")
label3.pack()
entry3 = tk.Entry()
entry3.pack()

calcular = tk.Button(text="Calcular", command=calcular_vt)
calcular.pack()

result_label = tk.Label(text="")
result_label.pack()

# Crédito
credit_label = tk.Label(janela, text='Desenvolvido por Yara de Oliveira Rufino', font=('Arial', 10), fg='gray')
credit_label.pack(side='bottom', padx=10, pady=10)
    
janela.mainloop()


# In[ ]:




