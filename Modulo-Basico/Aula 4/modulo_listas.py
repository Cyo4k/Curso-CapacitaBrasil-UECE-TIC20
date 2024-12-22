#modulo_listas.py

def encontrar_maximo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

def encontrar_minimo(lista):
    return min(lista)

def calcular_media(numeros):
    total = sum(numeros)
    quantidade = len(numeros)
    return total / quantidade
   

def ordenar_lista(lista):
    return sorted(lista)