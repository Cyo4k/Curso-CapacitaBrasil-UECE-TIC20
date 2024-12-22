"""#If
nota = float(input("Digite sua nota: "))

if nota >=7.0:
    print("Você está aprovado por média.")

if nota < 7.0:
    print("Você não está aprovado por média.")

#If else
#Serve para executar blocos de códigos que satisfaçam a condição se - senão

nota = float(input("Digite sua nota: "))
if nota >=7.0:
    print("Você está aprovado por média.")

else:
    print("Você não está aprovado por média.")


#Algaritmo para verificar se o numero é par com if - else 
numero = int(input("Digite um numero inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O numero é impar.")
"""


#elif
"""Em python, é usado para verificar múltiplas condições de forma sequencial
é uma combinação das palavras "else" e "if" e permite verificar outra condição
se a condição anterior falhar."""
"""
numero1 = float(input("Digite um número: "))

if numero1 > 0:
    print("O número é positivo.")
elif numero1 < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#Outro exemplo com elif pra verificar a idade

idade = int(input("Digite sua idade: "))

if idade < 5:
    print("Ingresso gratuito.")
elif idade <= 12:
    print("O preço do ingresso é R$ 10,00.")
elif idade <= 18:
    print("O preço do ingresso é R$ 15,00.")
elif idade <= 60:
    print("O preço do ingresso é R$ 20,00.")
else:
    print("O preço do ingresso é R$ 12,00.")

"""
#Estruta de repetição for
"""O comando for é usado para percorrer uma sequência, como uma lista, tupla, string ou
intervalo de números."""
"""
print("Repetição da lista com comando for")
frutas = ['maça', 'banana', 'cereja']
for fruta in frutas:
    print(fruta)

print("Comando range: range(5) gera números de 0 a 4")
#Exemplo 2 utilizando o comando range
for i in range(5): # range(5) gera números de 0 a 4
    print(i)
"""
#Comando While
"""Executa uma bloco de código enquanto uma condição
especificada for verdadeira."""
#Contagem regressiva
"""
print("Contagem regressiva")
contador = 5
while contador > 0:
    print(contador)
    contador -= 1 #Diminui o contador em 1 = 5 -1  = 4, 4-1 = 3

#Exemplo de utilização do while para checar se a senha está correta
senha_correta = "python123"
senha = ""
while senha != senha_correta:
    senha = input("Digite a senha: ")
    if senha != senha_correta:
        print("senha incorreta, tente novamente.")
        
        
print("Senha correta! Acesso concedido.")
"""
"""
#Acumulador
soma = 0
numero = 1
while numero <= 100:
    soma += numero
    numero += 1 #incrementa o número

print("A soma dos numeros de 1 a 100 é: ", soma)
        


#Cálculo de imposto
renda = float(input("Digite a renda anual: "))
if renda <= 2000:
    imposto = 0
elif renda <= 5000:
    imposto = renda * 0.1
else:
    imposto = renda * 0.2

print(f"O imposto a pagar é: R${imposto:.2f}")
"""

a=True
b=True
print(a and b)