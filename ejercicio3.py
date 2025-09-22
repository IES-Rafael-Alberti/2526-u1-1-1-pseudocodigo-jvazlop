# Pedimos un numero
x = int(input("Introduce un número: "))

# Dire que siempre es primo hasta que se compruebe

es_primo = True

# Los números menores o iguales a 1 no son primos

if x <= 1:
    es_primo = False
else:
    for i in range(2, x):
        if x % i == 0: 
# Y si encuentra un divisor

            es_primo = False

# Resultado:
    
if es_primo:
    print("El número es primo.")
else:
    print("El número no es primo.")