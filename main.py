# RPA - Automação de tarefas
# Primeira etapa:  Fazer um passo a passo do projeto -> O que será automatizado/quais os passos da tarefa ? 
    # Passo 1 - Entrar no sistema 
    # Passo 2 - Fazer Login 
    # Passo 3 - Ler a base de dados e importar os dados 
    # Passo 4 - Preencher os dados nos campos e cadastrar os produtos 
    # Passo 5 - Fazer a rotina/loop de repetição, cadastrando toda a base de dados

# Segunda etapa:  Desenvolver os passos
    # Passo 1 : 
        # Importar as bibliotecas
         
import pyautogui

#Faz a automação

# Para cliques -> pyautogui.click
# Para escrita -> pyautogui.write("texto")
# Para pressionar teclas -> pyautogui.press("win")
# Para utilizar atalhos de teclas ->  pyautogui.hotkey("ctrl","c")

import pandas as pd 

#Le e trata dados

# Para entrar no sistema , primeiro é preciso acessar a tecla Windows, buscar o chrome, entrar no app e acessar o site

# Acessar a pesquisa do Windows/aperta a tecla windows
pyautogui.press("win")

# Pesquisar o app Chrome
pyautogui.write("chrome")

# Acessar o app
pyautogui.press("enter")