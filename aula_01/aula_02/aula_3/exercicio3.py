import math

print("Digite a base e a altura do retângulo:")

base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura 
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"Área: {area}")
print(f"Perimetro: {perimetro}")
print(f"Diagonal: {diagonal}")