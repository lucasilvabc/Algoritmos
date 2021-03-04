"""
Seção 7 - Exercícios
"""

1:
larger = 0
number = int(input("Enter a number: "))
while number != 0:
    if number > larger:
        larger = number
print("Larger value " + str(larger))

2:
i = 0
while i <= 100:
    print(i)
    i = i + 1
    if (i % 10 == 0):
        print("Múltiplo de 10: " + str(i))

3:
i = 100
while i <= 200:
    print(i)
    i = i + 1
    if (i % 2 != 0):
        print("Ímpar: " + str(i))

4:
larger = 10
minor = 1
sum = larger + minor
i = 0
while i <= 10:
    print(i)
    i = i + 1
    while i < 0:
        print(i)
        if i > larger:
            larger = i
        if i < minor:
            minor = i
        sum = sum + i
print("Larger: " + str(larger))
print("Minor: " + str(minor))
print("Average: " + str(sum / 10))

5:
Name = input("Type your name: ")
print(Name)
Password = input("Type your password: ")
print(Password)
while Name == Password:
    print("Password can't be the same as the name")
    Name = input("Type your name: ")
    Password = input("Type your password: ")

6:
Number = int(input("Enter a number: "))
print(Number)
while Number > 10:
    print("Number must be less then 10")
    Number = int(input("Enter a number: "))
print("Tabuada de " + str(Number))
i = 0
while i <= 10:
    i = i + 1
    value = Number * i
    print(str(Number) + " X " + str(i) + " = " + str(value))

7:
id = int(input("Enter a mouse id: "))
print(id)

quantidade = 0
necessita_esfera = 0
necessita_limpeza = 0
necessita_troca_cabo = 0
quebrado = 0
print("Identifique o defeito:")
print("1 = necessita da esfera")
print("2 = necessita de limpeza")
print("3 = necessita troca de cabo ou conector")
print("4 = quebrado ou inutilizado")
defeito = int(input("Digite o defeito: "))
print(defeito)
if defeito == 1:
    necessita_esfera == necessita_esfera + 1
if defeito == 2:
    necessita_limpeza == necessita_limpeza + 1
if defeito == 3:
    necessita_troca_cabo == necessita_troca_cabo + 1
if defeito == 4:
    quebrado == quebrado + 1
quantidade = quantidade + 1
    

perc_esfera = (necessita_esfera * 100) / quantidade
perc_limpeza = (necessita_limpeza * 100) / quantidade
perc_cabo = (necessita_troca_cabo * 100) / quantidade
perc_quebrado = (quebrado * 100) / quantidade

print("Quantidade de mouses: " + str(quantidade))
print("Situação Quantidade Percentual")
print("1 = necessita da esfera " + str(necessita_esfera) + str(perc_esfera))
print("2 = necessita de limpeza " + str(necessita_limpeza) + str(perc_limpeza))
print("3 = necessita troca do cabo ou conector " + str(necessita_troca_cabo) + str(perc_cabo))
print("4 = quebrado ou inutizado " + str(quebrado + perc_quebrado))
