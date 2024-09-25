"""
Projeto: Login-bot
Descrição: Um simples bot que usa coordenadas para testar login e senha em qualquer aplicativo.
Autor: Bugattiaob
Data: Tue, September 24, 2024
Licença: GPL
Copyright (c) 2024 Bugattiaob. Todos os direitos reservados.
"""


import pyautogui
import keyboard

# Função para testar login
def test_login(password): #def test_login(username, password):
    # Defina as coordenadas do campo de usuário e senha aqui
    # username_field_x, username_field_y = 450, 250  # Exemplo de coordenadas
    password_field_x, password_field_y = 450, 250  # Exemplo de coordenadas
    login_button_x, login_button_y = 450, 330  # Exemplo de coordenadas

    # Preenche o campo de usuario
    # pyautogui.click(username_field_x, username_field_y)
    # pyautogui.typewrite(username)
    
    # Preenche o campo de senha
    pyautogui.click(password_field_x, password_field_y)
    pyautogui.typewrite(password)

    # Clica no botão de login
    pyautogui.click(login_button_x, login_button_y)
    
# Função principal
def start_bot(accounts):
    for password in accounts: #for username, password in accounts:
        test_login(password) #test_login(username, password)
        if keyboard.is_pressed('End'):  # Para se a tecla "End" for pressionada
            print("Bot interrompido.")
            break

# Lista de contas ou senhas
accounts = [
    # ("usuario", "senha"),
    ("senha"), 
]

# Inicia o bot
start_bot(accounts)

