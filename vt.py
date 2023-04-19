#!/usr/bin/env python
# coding: utf-8

# In[36]:


from datetime import datetime, timedelta
from workadays import workdays as wd
import tkinter as tk

janela = tk.Tk()
janela.geometry("300x250")
janela.title('Calculadora de VT')

def calcular_vt():
    try:
        data_inicio = datetime.strptime(entry1.get(), "%d/%m/%Y").date()
        data_fim = datetime.strptime(entry2.get(), "%d/%m/%Y").date()
        if data_inicio > data_fim:
            result_label.config(text="A data de início deve ser anterior à data de término")
            return
        vt = entry3.get()
        if vt == "":
            result_label.config(text="Por favor, insira o valor do Vale Transporte")
            return
        vt = float(vt.replace(",", "."))
        dias_trabalhado = wd.networkdays(data_inicio, data_fim, country='BR', state='SP')
        total_vt = vt * dias_trabalhado
        result = f"Total de dias trabalhados no período: {dias_trabalhado}\nTotal do vale transporte: R$ {total_vt:.2f}"
        result_label.config(text=result)

    except ValueError as e:
        if "does not match format" in str(e):
            message = "Formato de data incorreto.\nPor favor, insira as datas no formato dd/mm/aaaa"
        else:
            message = str(e)
        result_label.config(text=message)

#data de inicio do período a ser calculado
label1 = tk.Label(text="Data de início (dd/mm/aaaa):")
label1.pack()
entry1 = tk.Entry()
entry1.pack()

#data final do período a ser calculado
label2 = tk.Label(text="Data de término (dd/mm/aaaa):")
label2.pack()
entry2 = tk.Entry()
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




