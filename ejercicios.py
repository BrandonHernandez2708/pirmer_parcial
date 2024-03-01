#Escribe una función en Python que reciba una lista como parámetro y
#devuelva la suma de todos los
#elementos de la lista.
lista=[1,2,3,4,5,6]
texto="python"
def suma_lista(lista):
    suma=0
    for elemento in lista:
        suma +=elemento
    return suma
print(suma_lista(lista))
#2.define una función llamada "inverso_palabra" que reciba una cadena
#como parámetro y devuelva la
#cadena invertida. Por ejemplo, si la entrada es "python", la salida
#debería ser "nohtyp".
def inverso_palabra(texto):
    inverso= print (("python")[::-1])
    return inverso
    
print(inverso_palabra(texto))

#Escribe un programa que pida al usuario una lista de números y luego
#imprima la suma de los números
#pares en la lista.
numeros = input("Ingrese una lista de números separados por espacio: ").split()
numeros = [int(num) for num in numeros]
sumas_pares = sum(num for num in numeros if num % 2 == 0)
print("La suma de los números pares es:", sumas_pares)
#Crea un diccionario en Python que represente un libro, con claves como "título", "autor" y "año de
#publicación". Luego, escribe un código que agregue un nuevo campo al #diccionario, como "género", y
#lo imprima.
libro=[]
datos={"titulo":"don quijote de la mancha","Autor":"Miguel cervantes","Año":"1605"}
libro.append(datos)
g={"Genero":"Novela literaria"}
libro.append(g)
print(libro)