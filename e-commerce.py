import random

print('Loja BielzTech')
print(" ")

print(" ")

name =  input('Nome do Cliente: ')
cpf  =  input("CPF: ")
birthday  =  input('Data de Nascimento: ')
def gerar_id_cliente():
  min_num = 1000000000
  max_num = 9999999999
  id_cliente = random.randint(min_num, max_num)
  return id_cliente

id_codigo = gerar_id_cliente()

print(" ")

print(f"Seja bem vindo {name} a Loja BielzTech, seu código de cliente é {id_codigo}")

# ------------------------------------------------------------------------------
# BANCO DE DADOS DOS PRODUTOS
# (1) - COMPUTADORES
def lista_computador():
        print('''
          1 - Computador Completo Intel Core i7 16GB SSD 480GB Monitor 19" 4 Núcleos Super Turbo Pc Hdmi Teclado e Mouse Strong Tech
          2 - Computador Pc Completo i5 3° Geração 8gb Hd 500GB Wi-fi C/Webcam
          3 - Computador Completo Fácil Intel Core I7 3.4GHz 16GB SSD 960GB Monitor 21" HDMI LED Teclado e Mouse - Fácil Computadores
        ''')

def escolher_computador01():
    id01_computador = "Computador Completo Intel Core i7 16GB SSD 480GB Monitor 19 4 Núcleos Super Turbo Pc Hdmi Teclado e Mouse Strong Tech"
    print(id01_computador)

def escolher_computador02():
    id02_computador = "Computador Pc Completo i5 3° Geração 8gb Hd 500GB Wi-fi C/Webcam"
    print(id02_computador)

def escolher_computador03():
    id03_computador = "Computador Completo Fácil Intel Core I7 3.4GHz 16GB SSD 960GB Monitor 21 HDMI LED Teclado e Mouse - Fácil Computadores"
    print(id03_computador)

def aviso_pagamento():
      print('''
      (1) - Dinheiro
      (2) - Débito
      (3) - Crédito (24x)
    ''')

def forma_pagamento1():
    forma_dinheiro = "Dinheiro a Vista"
    print(forma_dinheiro)

def forma_pagamento2():
    forma_debito = "Débito"
    print(forma_debito)

def forma_pagamento3():
    forma_credito = "Crédito (24x)"
    print(forma_credito)

def despedida():
    print(f'''Compra efetuada com sucesso!
    Código do cliente -> {id_codigo}
    Obrigado por comprar conosco!
    ''')
# ------------------------------------------------------------------------------
# (2) - CONSOLES
def lista_console():
        print('''
          1 - Xbox One
          2 - Playstation 4
          3 - Nintendo Switch
        ''')

def escolher_console01():
    id01_console = "Xbox One"
    print(id01_console)

def escolher_console02():
    id02_console = "Playstation 4"
    print(id02_console)

def escolher_console03():
    id03_console = "Nintendo Switch"
    print(id03_console)

def aviso_pagamento():
      print('''
      (1) - Dinheiro
      (2) - Débito
      (3) - Crédito (24x)
    ''')

def forma_pagamento1():
    forma_dinheiro = "Dinheiro a Vista"
    print(forma_dinheiro)

def forma_pagamento2():
    forma_debito = "Débito"
    print(forma_debito)

def forma_pagamento3():
    forma_credito = "Crédito (24x)"
    print(forma_credito)

def despedida():
    print(f'''Compra efetuada com sucesso!
    Código do cliente -> {id_codigo}
    Obrigado por comprar conosco!
    ''')
# ------------------------------------------------------------------------------
# (3) - CELULARES
def lista_celulares():
        print('''
          1 - Apple iPhone 15 Pro Max (256 GB) — Titânio Azul
          2 - Smartphone Moto G14 128GB 4GB RAM Grafite
          3 - Xiaomi Redmi Note 9 128 GB Verde - Outlet
        ''')

def escolher_celular01():
    id01_celular = "Apple iPhone 15 Pro Max (256 GB) — Titânio Azul"
    print(id01_celular)

def escolher_celular02():
    id02_celular = "Smartphone Moto G14 128GB 4GB RAM Grafite"
    print(id02_celular)

def escolher_celular03():
    id03_celular = "Xiaomi Redmi Note 9 128 GB Verde - Outlet"
    print(id03_celular)

def aviso_pagamento():
      print('''
      (1) - Dinheiro
      (2) - Débito
      (3) - Crédito (24x)
    ''')

def forma_pagamento1():
    forma_dinheiro = "Dinheiro a Vista"
    print(forma_dinheiro)

def forma_pagamento2():
    forma_debito = "Débito"
    print(forma_debito)

def forma_pagamento3():
    forma_credito = "Crédito (24x)"
    print(forma_credito)

def despedida():
    print(f'''Compra efetuada com sucesso!
    Código do cliente -> {id_codigo}
    Obrigado por comprar conosco!
    ''')
# ------------------------------------------------------------------------------
# (4) - NOTEBOOKS
def lista_notebooks():
        print('''
          1 - Notebook Acer Aspire 5 A515 Ryzen 7 5700u 512gb 8gb Ram W11
          2 - Samsung Book Celeron-6305, 4G, 256GB SSD, Intel UHD, 15.6"FHD, W11 Cinza
          3 - Apple notebook MacBook Air (de 13 polegadas, Processador M1 da Apple com CPU 8‑core e GPU 7‑core, 8 GB RAM, 256 GB) - Prateado
        ''')

def escolher_notebook01():
    id01_notebook = "Notebook Acer Aspire 5 A515 Ryzen 7 5700u 512gb 8gb Ram W11"
    print(id01_notebook)

def escolher_notebook02():
    id02_notebook = "Samsung Book Celeron-6305, 4G, 256GB SSD, Intel UHD, 15.6 FHD, W11 Cinza"
    print(id02_notebook)

def escolher_notebook03():
    id03_notebook = "Apple notebook MacBook Air (de 13 polegadas, Processador M1 da Apple com CPU 8‑core e GPU 7‑core, 8 GB RAM, 256 GB) - Prateado"
    print(id03_notebook)

def aviso_pagamento():
      print('''
      (1) - Dinheiro
      (2) - Débito
      (3) - Crédito (24x)
    ''')

def forma_pagamento1():
    forma_dinheiro = "Dinheiro a Vista"
    print(forma_dinheiro)

def forma_pagamento2():
    forma_debito = "Débito"
    print(forma_debito)

def forma_pagamento3():
    forma_credito = "Crédito (24x)"
    print(forma_credito)

def despedida():
    print(f'''Compra efetuada com sucesso!
    Código do cliente -> {id_codigo}
    Obrigado por comprar conosco!
    ''')
#-------------------------------------------------------------------------------
def parar(escolha):
    if escolha != 'opcao_computador' or 'opcao_console' or 'opcao_celular' or "opcao_notebook":
       print('Escolha incorreta')

def loja():
    print('''
      (1) - Computador
      (2) - Console
      (3) - Celular
      (4) - Notebook
    ''')
    opcao_produto = input('Escolha uma das opções de produtos acima: ')
# ------------------------------------------------------------------------------
# (1) - COMPUTADORES
    if opcao_produto ==  '1':
      lista_computador()
      escolha_computador = input('Escolha o computador acima: ')
      if escolha_computador == "1":
         escolher_computador01()
         aviso_pagamento()
      elif escolha_computador == "2":
         escolher_computador02()
         aviso_pagamento()
      elif escolha_computador == "3":
         escolher_computador03()
         aviso_pagamento()
      escolher_pagamento = input('Escolha a forma de pagamento acima: ')
      if escolher_pagamento == "1":
          forma_pagamento1()
          despedida()
      elif escolher_pagamento == "2":
          forma_pagamento2()
          despedida()
      elif escolher_pagamento == "3":
          forma_pagamento3()
          despedida()
# ------------------------------------------------------------------------------
  # (2) - CONSOLES
    if opcao_produto ==  '2':
      lista_console()
      escolha_console = input('Escolha o console acima: ')
      if escolha_console == "1":
         escolher_console01()
         aviso_pagamento()
      elif escolha_console == "2":
         escolher_console02()
         aviso_pagamento()
      elif escolha_console == "3":
         escolher_console03()
         aviso_pagamento()
      escolher_pagamento = input('Escolha a forma de pagamento acima: ')
      if escolher_pagamento == "1":
          forma_pagamento1()
          despedida()
      elif escolher_pagamento == "2":
          forma_pagamento2()
          despedida()
      elif escolher_pagamento == "3":
          forma_pagamento3()
          despedida()
# ------------------------------------------------------------------------------
  # (3) - CELULARES
    if opcao_produto ==  '3':
      lista_celulares()
      escolha_celular = input('Escolha o celular acima: ')
      if escolha_celular == "1":
         escolher_celular01()
         aviso_pagamento()
      elif escolha_celular == "2":
         escolher_celular02()
         aviso_pagamento()
      elif escolha_celular == "3":
         escolher_celular03()
         aviso_pagamento()
      escolher_pagamento = input('Escolha a forma de pagamento acima: ')
      if escolher_pagamento == "1":
          forma_pagamento1()
          despedida()
      elif escolher_pagamento == "2":
          forma_pagamento2()
          despedida()
      elif escolher_pagamento == "3":
          forma_pagamento3()
          despedida()
# ------------------------------------------------------------------------------
  # (4) - NOTEBOOKS
    if opcao_produto ==  '4':
      lista_notebooks()
      escolha_notebook = input('Escolha o notebook acima: ')
      if escolha_notebook == "1":
         escolher_notebook01()
         aviso_pagamento()
      elif escolha_notebook == "2":
         escolher_notebook02()
         aviso_pagamento()
      elif escolha_notebook == "3":
         escolher_notebook03()
         aviso_pagamento()
      escolher_pagamento = input('Escolha a forma de pagamento acima: ')
      if escolher_pagamento == "1":
          forma_pagamento1()
          despedida()
      elif escolher_pagamento == "2":
          forma_pagamento2()
          despedida()
      elif escolher_pagamento == "3":
          forma_pagamento3()
          despedida()

while True:
      loja()
