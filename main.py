#ejercicio 1
print("Ejercicio 1:")
import math
print(math.pi)
def area_circulo(radio):
  return (radio **2) * math.pi
radio = int(input("Introduzca el radio de su circulo:"))
print("El área de su circulo es:", (area_circulo(radio)))
print("")

#ejercicio 2 
print("Ejercicio 2:")
def mayor(lista):
  return max(lista)
def lee_numero():
  lista=[]
  for i in range (0,3):
    numero= int(input(f"Introduce el número{i}:"))
    lista.append(numero)
  return mayor(lista)
print(lee_numero())
print("")

#ejercicio 3
print("Ejercicio 3:")
def imc(peso, altura): 
  imc= peso / (altura*altura)
  if imc<18.5:
  