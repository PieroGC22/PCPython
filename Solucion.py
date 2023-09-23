1
nombre_usuario = input ("Escribe tu nombre: ")
print ("Hola, " + nombre_usuario + " ")

#2
monto_consumo = float(input("¿Cuanto fue su consumo?"))
porcentaje_propina = float(input("¿Cuanto desea dejar de propina?"))
propina = (monto_consumo*porcentaje_propina)/100
print(f"Dejaras de propina: {propina:.2f}")

#3
cant_payasos = int(input("Ingrese el numero de payasos vendidos: "))
cant_muñecas = int(input("Ingrese el numero de muñecas vendidas: "))
peso_payaso = 112
peso_muñeca = 75
peso_total = (cant_payasos * peso_payaso) + (cant_muñecas * peso_muñeca)
print(f"El peso total del paquete que será enviado es de {peso_total} gramos.")

#4
N = int(input("Por favor, ingrese un entero positivo N: "))
suma = 0
if N < 1:
    print("N debe ser un entero positivo.")
else:
    for i in range(1, N + 1):
        suma += i
    print(f"La suma de todos los enteros desde 1 hasta {N} es {suma}.")

#5
cant_shows = int(input("Ingrese cuántos shows musicales ha visto en el último año: "))
ha_visto_mas_de_3 = cant_shows > 3
print("¿Ha visto más de 3 shows musicales en el último año?", ha_visto_mas_de_3)

#6
edad = int(input("Por favor, ingrese su edad: "))
if edad < 4:
    precio_entrada = 0
elif 4 <= edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10
print(f"El precio de la entrada es: ${precio_entrada}")

#7
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
print("Seleccione una opción:")
print("1. Mostrar la suma de los dos números.")
print("2. Mostrar la resta del primer número menos el segundo número.")
print("3. Mostrar la multiplicación de los dos números.")
opcion = input("Elija una opción (1/2/3): ")
if opcion == '1':
    resultado = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es igual a {resultado}")
elif opcion == '2':
    resultado = numero1 - numero2
    print(f"La resta de {numero1} menos {numero2} es igual a {resultado}")
elif opcion == '3':
    resultado = numero1 * numero2
    print(f"La multiplicación de {numero1} y {numero2} es igual a {resultado}")
else:
    print("Opción no válida. Por favor, elija 1, 2 o 3.")

#9
lista_original = ['Di', 'buen', 'dia', 'a', 'papa']
lista_invertida = lista_original[::-1]
print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)

#10
mi_lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
posc_a_eliminar = [0, 4, 5]
for posicion in sorted(posc_a_eliminar, reverse=True):
    if 0 <= posicion < len(mi_lista):
        mi_lista.pop(posicion)
print("Lista nueva:")
print(mi_lista)

#11
mi_lista = [1, 2, 2, 3, 4, 4, 5]
conj_sin_duplicados = set(mi_lista)
lista_sin_duplicados = list(conj_sin_duplicados)
print("Lista original:", mi_lista)
print("Lista sin duplicados:", lista_sin_duplicados)
