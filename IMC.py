#Variaveis
resultado = ""
peso = 0
altura = 0
imc = 0

print("Qual é o seu peso? ")
peso = float(input()) 
print("Qual é a sua altura? ")
altura = float(input()) 

#Calculo de IMC
imc = peso / (altura * altura)

if imc > 40:
    resultado = "Obesidade grau 3"
elif imc >= 35 and imc <= 39.9:
    resultado = "Obesidade grau 2"
elif imc >= 30 and imc <= 34.9:
    resultado = "Obesidade grau 1"
elif imc >= 25 and imc <= 29.9:
    resultado = "Sobrepeso"
elif imc >= 18 and imc <= 24.9:
    resultado = "Normal"
else:
    resultado = "Abaixo do peso"

#Printando calculo de IMC e resultado
print(f"Seu IMC É:{imc: .2f}" ,"",resultado)