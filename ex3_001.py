"""
Programa soma
Descrição: lê dois números do teclado, calcula a sua soma e imprime na tela seu resultado.
Autor: Augusto Jacques
Data: 25/02/2025
Versão: 0.0.1
"""

# Alocação de memória

num_1 = 0
num_2 = 0

# entrada de dados

num_1 = int(input("\nQual o primeiro número a ser somado?"))
num_2 = int(input("\nQual o segundo número a ser somado?"))

# processamento de dados

resultado = num_1 + num_2

# saída de dados

print(f"O resultado de {num_1} + {num_2} é igual a {resultado}.")