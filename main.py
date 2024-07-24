import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
import customtkinter as ctk

def valida_cpf(cpf_enviado_usuario):
    cpf_enviado_usuario = ''.join(filter(str.isdigit, cpf_enviado_usuario))
    if len(cpf_enviado_usuario) != 11:
        return False
    if cpf_enviado_usuario == cpf_enviado_usuario[0] * 11:
        return False

    nove_digitos = cpf_enviado_usuario[:9]
    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
    return cpf_enviado_usuario == cpf_gerado_pelo_calculo

def format_cpf(event=None):
    cpf = cpf_entry.get().replace(".", "").replace("-", "")
    new_text = ""

    for index in range(len(cpf)):
        if index in [3, 6]:
            new_text += "."
        elif index == 9:
            new_text += "-"
        new_text += cpf[index]

    cpf_entry.delete(0, tk.END)
    cpf_entry.insert(0, new_text)

def limitar_tamanho(string):
    if len(string) > 14:  # 11 dígitos + 3 caracteres de formatação
        return False
    return all(char.isdigit() or char in ".-" for char in string)

def validar_cpf():
    cpf = cpf_entry.get().replace(".", "").replace("-", "")
    if valida_cpf(cpf):
        msg = f"{cpf} é válido"
        color = "green"
    else:
        msg = "CPF inválido"
        color = "red"

    dialog = tk.Toplevel(root)
    dialog.geometry("300x100")
    dialog.title("Validação de CPF")

    label = tk.Label(dialog, text=msg, font=("Helvetica", 14), fg=color)
    label.pack(padx=20, pady=20)

# Criar a janela principal usando ttkbootstrap
root = tb.Window(themename="superhero")
root.title("Validador de CPF")

# Configurar a janela principal
root.geometry("500x300")
root.resizable(False, False)

# Criar e configurar o título
title_label = ttk.Label(root, text="Validador de CPF", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

# Criar e configurar a mensagem de instrução
instruction_label = ttk.Label(root, text='Digite um CPF e clique em "Validar CPF" para verificar se ele é válido ou falso', font=("Helvetica", 10))
instruction_label.pack(pady=5)

# Criar e configurar o campo de entrada
cpf_entry = ttk.Entry(root, validate="key", font=("Helvetica", 14), width=20, validatecommand=(root.register(limitar_tamanho), '%P'))
cpf_entry.pack(padx=10, pady=10)
cpf_entry.bind("<KeyRelease>", format_cpf)

# Criar e configurar o botão para validar o CPF
validar_button = ttk.Button(root, text="Validar CPF", command=validar_cpf, style="success.TButton")
validar_button.pack(padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
