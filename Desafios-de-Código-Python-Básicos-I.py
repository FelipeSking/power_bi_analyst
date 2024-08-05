# Descrição
#Calcular a média é uma das operações estatísticas mais básicas e úteis para resumir um conjunto de dados. Dada uma lista de números, você deve calcular a média aritmética desses números.
#Entrada
#Uma lista de números. Por exemplo:10, 20, 30, 40, 50.

#Saída
#Um número representando a média dos números na lista. Por exemplo: 30.0. O que fazer: Somar todos os números e dividir pela quantidade de elementos na lista.

# Explicação do Código: 

# - Conversão para Lista: Utilizamos float para converter os elementos da lista de strings para números de ponto flutuante.

# - Cálculo da Soma: Utilizamos a função sum para calcular a soma de todos os números na lista.

# - Cálculo da Quantidade: Utilizamos len para calcular o número de elementos na lista.

# - Cálculo da Média: Dividimos a soma pela quantidade de elementos para obter a média.




# Receber a lista do usuário
entrada = input()
# Convertee a string de entrada em uma lista de números
lista = [float(x.strip()) for x in entrada.split(',')]

# Calcula a soma dos números na lista
soma = sum(lista)
# Calcula a quantidade de elementos na lista
quantidade = len(lista)
# TODO: Calcule a média aritmética:
media = soma / quantidade

# Exibir a média com duas casas decimais
print(f'{media:.1f}')
