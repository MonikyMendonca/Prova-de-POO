import random

def gerar_matriz(tamanho):
    return [[random.randint(1, 10) for _ in range(tamanho)] for _ in range(tamanho)]


def multiplicacao_de_matrizes(matriz_a, matriz_b):
    tamanho = len(matriz_a)
    
    res= [[0 for _ in range(tamanho)] for _ in range(tamanho)]
    
    for i in range(tamanho): 
        for j in range(tamanho):  
            for k in range(tamanho): 
                res[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return res

def exibir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{valor:4}" for valor in linha))

def main():

    tamanho = int(input("Digite o tamanho da matriz quadrada: "))

    matriz_a = gerar_matriz(tamanho)
    matriz_b = gerar_matriz(tamanho)

    print("\nMatriz A:")
    exibir_matriz(matriz_a)

    print("\nMatriz B:")
    exibir_matriz(matriz_b)

    
    matriz_resultado = multiplicacao_de_matrizes(matriz_a, matriz_b)

    print("\nResultado da Multiplicação (A * B):")
    exibir_matriz(matriz_resultado)

if __name__ == "__main__":
    main()
