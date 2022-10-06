
n = int(input("Digita un número entero y positivo: "))
n1 = n
1234

if n >= 0:
    suma = 0
    while n > 0:
        suma = suma + n % 10
        n = n // 10
    print("La suma de", n1, "es:", suma)
else:
    print("El numero debe ser entero y positivo")