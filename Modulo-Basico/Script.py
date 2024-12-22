lista = [1, 2, 3, 'quatro', 5.0]

print(lista)

#tupla é tipo uma lista porem só podem ser inseridas em seu conteudo o mesmo tipo de dado
tupla = (1, 2, 3, 4, 5)
print(tupla)


#Algoritmo 1
#Calcular a média de um aluno
#solicitar notas com o comando input

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a primeira nota: "))
nota3 = float(input("Digite a primeira nota: "))

#calcular a média das notas
media = (nota1+nota2+nota3)/3

#Exibir a média
print("A média das três notas é: ",media)


#Algoritmo 2
#Calcular a quantidade de segundos a partir do valor em horas digitado pelo usuário.
#Solicitar que o usuário insira o numero de horas com o comando input

horas = float(input("Digite o número de horas: "))

#Converter horas em segundo 1minutos tem 60 segundos e uma hora possui 60minutso então basta multiplicar
# 60*60 que o resultado será 3600
segundos = horas*3600

#Exibir o resultado
print("Total de segundos: ", segundos)

#Algoritmo 3
#Calcular o quadrado de dois números digitados
#Solciitar ao usuário os dois números

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

#Calcular o quadrado dos números

quadrado1 = numero1**2
quadrado2 = numero2**2

#Exibir resultado

print(f"O quadrado de {numero1} é: {quadrado1}")
print(f"O quadrado de {numero2} é: {quadrado2}")
