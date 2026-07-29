Altura = float(input("Digite sua Altura."))
Peso  = float(input("Digite seu Peso aqui"))
AlturaIMC = Altura**2
IMC = Peso/AlturaIMC
print (f"seu Imc é {IMC:.2f}")
if IMC <= 18.4:
    print ("Você está abaixo do peso")
elif IMC >= 18.5 and IMC <=24.9:
    print("você está com o peso em dia, está saudavel!")
elif IMC >=25 and IMC <=29.9:
    print("você está acima do seu peso, por favor trate isso pelo bem da sua saude")
elif IMC>=30 and IMC<=34.9 :
    print("Você esta com um grau de obsidade I, va ao medico")
elif IMC >=35 and IMC<=39.9:
    print("você está com um Grau de obsidade II, va ao Medico Urgente")
else:
    print("você está com um Grau de obsidade nivel III, vá a um medico AGORA!")



