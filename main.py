# RPA - Automação de tarefas
# Primeira etapa:  Fazer um passo a passo do projeto -> O que será automatizado/quais os passos da tarefa ? 
    # Passo 1 - Entrar ano sistema 
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


import time
# Usado aqui para setar intervalos de tempo 

# Para entrar no sistema , primeiro é preciso acessar a tecla Windows, buscar o chrome, entrar no app e acessar o site

#Pausa entre as tarefas
pyautogui.PAUSE = 1

# Acessar a pesquisa do Windows/aperta a tecla windows
pyautogui.press("win")

# Pesquisar o app Chrome
pyautogui.write("chrome")

# Acessar o app
pyautogui.press("enter")

# Digital o link do site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# Acessar o site
pyautogui.press("enter")

# Aguardar o carregamento do site
time.sleep(8)


    # Passo 2 : 
        # Fazer Login

# Point(x=674, y=380)
pyautogui.click(x=674, y=380)

email = "email@email.com"
senha = "p@ssw0rd"

#Fazer Login 
pyautogui.write(email)

# Avançar para o próximo campo
pyautogui.press("tab")

# Digitar a senha 
pyautogui.write(senha)

# Avança para o login - pode ser tab ou position
pyautogui.press("tab")

# Entra na plataforma
pyautogui.press("enter")

    # Passo 3 :
        # Ler a base de dados e importar os dados 

# Ler a tabela dos dados 
tabela = pd.read_csv("produtos.csv")

# Cadastrar os campos para cada produto 
for linhas in tabela.index:

# Colunas : codigo | marca | tipo | categoria numero| preco_unitario numero| custo numero| obs tem vazios


    # Clicar no primeiro campo para iniciar o cadastro dos produtos
    pyautogui.doubleClick(x=493, y=253)

    # Codigo do produto
    codigo = tabela.loc[linhas,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")


    # Marca do produto        
    pyautogui.write(tabela.loc[linhas,"marca"])
    pyautogui.press("tab")


    # Tipo do produto
    pyautogui.write(tabela.loc[linhas,"tipo"])
    pyautogui.press("tab")


    # Categoria do produto
    pyautogui.write(str(tabela.loc[linhas,"categoria"]))
    pyautogui.press("tab")


    # Preço unitário do produto
    pyautogui.write(str(tabela.loc[linhas,"preco_unitario"]))
    # Pode ser str(123) ou "123" sempre que for numero
    pyautogui.press("tab")


    # Custo do produto
    pyautogui.write(str(tabela.loc[linhas,"custo"]))
    pyautogui.press("tab")

    # OBS
    obs = tabela.loc[linhas,"obs"]
    if not pd.isna(obs):
        # condição para tratar obs vazio
        pyautogui.write(obs)
        # poderia ser feito com str() porem o campo ficaria preenchido com NaN

    pyautogui.press("tab")

    # Cadastrar/Enviar o produto
    pyautogui.press("enter")

    # Volta para o topo da página 
    pyautogui.scroll(2000)
    # Caso seja scroll para baixo -> colocar o numero negativo - ex: -2000

