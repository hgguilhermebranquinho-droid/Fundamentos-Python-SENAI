Salario = float(input("Você poderia me falar quanto você ganha para mim calcular o seu salrio bruto?"))
Inss = (Salario/100)*8
Sindicato = (Salario/100)*5
Ir = (Salario/100)*11
Liquido = Salario - (Ir + Sindicato + Inss)
print(f"foi descontado de você {Inss} de inss, {Sindicato} de sindicato e {Ir} de Imposto de renda e sobrou foi {Liquido}")