import numpy as np

# Define uma matriz quadrada
matriz = np.array([
    [4, 7],
    [2, 6]
])

# Verifica se a matriz tem determinante não nulo
determinante = np.linalg.det(matriz)
if determinante == 0:
    print("A matriz é singular e não pode ser invertida.")
else:
    # Calcula a matriz inversa
    matriz_inversa = np.linalg.inv(matriz)
    
    print("Matriz original:")
    print(matriz)

    print("\nMatriz inversa:")
    print(matriz_inversa)

    # Verifica a propriedade da matriz inversa
    # Produto da matriz original pela matriz inversa deve ser a matriz identidade
    identidade = np.dot(matriz, matriz_inversa)
    print("\nProduto da matriz original pela matriz inversa (deve ser identidade):")
    print(identidade)
