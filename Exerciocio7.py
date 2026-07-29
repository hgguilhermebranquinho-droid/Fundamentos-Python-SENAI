Ano = int(input("qual ano você nasceu? quero ver se ele e bissexto"))
if (Ano % 4 == 0 and Ano % 100 != 0 ) or Ano % 400 == 0:
    print ("ele é bissexto")
else: 
    print("ele é um ano normal")