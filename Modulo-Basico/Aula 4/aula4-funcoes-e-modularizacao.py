#Funções
"""São blocos de códigos que realizam uma tarefa especifica
são trechos de códigos que podem ser reutilizados em diferentes parte de um programa
são fundamentais na programação porque permite encapsular em um conjunto de instruções que executam 
determinada operação
"""

#Exemplo o codigo de acalulcar a area
"""
largura = 3
altura = 2

area = largura*altura

print(area)
"""
#Exemplo do codigo como função
#A palavra def é reserva para definir uma função.

def calcular_area(largura, altura):
    area = largura*altura
    return area

#Declaração e passagem de parametros
"""A declaração de uma função: é o processo de definir uma função com um nome
, parâmetros(opcional) e um corpo que contém um bloco de código a ser executado
quando a função é chamada.
Passagem de parâmetros: ato de fornecer argumentos para a função quando ela é chamada"""

#Elementos de uma função em python
"""Nome: identifica a função e é usada para chamá-la
Parâmetros: são variáveis que a função espera receber quando é chamada. Eles são
opcionais e podem ser utilizados para fornecer dados à função para serem processados.
Corpo: Contém as intruncões que a função executa quando é chamada.
Retorno: Algumas funções retornam um valor com resultado de seu processamento, 
utilizando a palavra chave return."""
#Exemplo
"""
def imprimirNome(nome):
#Função que imprime uma saudação.
    print(f"Olá, {nome}!")

#chamada da função
imprimirNome("Jose")
#Saída: Olá, Jose!

#Outro exemplo de função

def eh_par(numero):
    return numero % 2 == 0
#chamda da função e imprimindo o resultado

numero = 10
if eh_par(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
"""

#Modularização de código
"""A modularização é a prática de dividir um programa extenso em partes menores e mais manejáveis, chamdas módulos.
Isso melhora a manutenção, facilita a reutilização de código e organiza o projeto de forma mais eficiente.
Em python, os módulos são implementados com arquivo .py."""
#meu_projeto/
    #principal.py
    #modulo_matematica.py
    #modulo_listas.py

#principal.py

def exemplo(x, y=10):

    return x * y

print(exemplo(5))