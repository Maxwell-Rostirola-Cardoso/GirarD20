import random

dados = int(input("Quantos dados de 20 lados serão rolados: "))

for i in range(dados):
    numero = random.randint(1,20)

    print(f"Repetição {i + 1}: {numero}")

#print(random.random()) -> randon com número ponto flutuante
#print(random.randint(1,20)) -> random de número inteiro, mas é necessário definir os valores
