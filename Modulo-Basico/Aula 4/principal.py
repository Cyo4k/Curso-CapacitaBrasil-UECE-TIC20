from modulo_matematica import somar, subtrair, multiplicar, dividir

from modulo_listas import encontrar_maximo, encontrar_minimo, ordenar_lista, calcular_media

def main():
    
    #Usando funções do modulo_matematica
    soma = somar(3,5)    
    subtracao = subtrair(10,4)
    print("A soma é: ", soma)
    print("A subtração é: ", subtracao)

    #usando funções do modulo_listas
    lista = [10,20,30,40,50]
    print(f"O maior número da lista {lista} é {encontrar_maximo(lista)}")

    #chamando a função Calular média em uma lista e imprimindo o resultado.
    numeros = [10,20,30,40,50]
    print(f"A média dos numeros {numeros} é {calcular_media(numeros)}")
    
    #Chamando a função de ordenar lista

    numeros = [10,20,30,40,50]
    print(f"A Lista {numeros} ordenada é  {ordenar_lista(numeros)}")

   
    

if __name__ == "__main__":
    main()