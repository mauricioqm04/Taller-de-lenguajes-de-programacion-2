print("Hello, World!")


if 5 > 2:
  print("Five is greater than two!")

#Error (#This is a comment.)
"""if 5 > 2:
	print("Five is greater than two!")

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#Error
if 5 > 2:
	print("Five is greater than two!")
    print("Five is greater than two!")
"""
"""
This is a comment
written in
more than just one line
"""

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Si desea especificar el tipo de datos de una variable, puede hacerlo con la conversión.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Obtener el tipo
x = 5
y = "John"
print(type(x))
print(type(y))

#Distingue mayúsculas y minúsculas
a = 4
A = "Sally"
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Desempaquetar una colección
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Variables de salida

x = 5
y = "John"
print(x, y)

#Error 
#x = 5
#y = "John"
#print(x + y)

####Variables globales
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

####Variables
x = "awesome" #Variable global

def myfunc():
  x = "fantastic" #Variable local
  print("Python is " + x) #Imprime con variable local

myfunc()

print("Python is " + x) #Imprime con variable global

#Global dentro de una funcional
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Obtener tipo de dato de variable
x = 5
print(type(x))

"""
Tipos de datos

x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
"""

#Conversion de tipo
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)
######Nota: No puede convertir números complejos en otro tipo de número.

# Random
import random

print(random.randrange(1, 10))


#String
a = "Hello, World!"
print(a[1]) #Imprime la posicion 1 de la cadena 

for x in "banana":
  print(x) #Imprime todas la letras de a una

#Longitud de string
a = "Hello, World!"
print(len(a))

#Comprobar cadena
#Compruebe si "gratis" está presente en el siguiente texto:

txt = "The best things in life are free!"
print("free" in txt)

#En un condicional
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Si no esta presente
txt = "The best things in life are free!"
print("expensive" not in txt)

#Rango de un String
b = "Hello, World!"
print(b[2:5])

#Concatenar cadenas
a = "Hello"
b = "World"
c = a + b
print(c)

#Concatenar cadenas y numeros
age = 36
txt = "My name is John, and I am {}" #Debe llevar corchetes
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Para asegurar que quedan en la posicion correcta
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Algunos valores en BOOL son falsos
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Si tienen algn dato son True

#la isinstance() función, que se puede usar para determinar si un objeto es de cierto tipo de datos:
x = 200
print(isinstance(x, int))

"""
Operadores de identidad de Python
Los operadores de identidad se utilizan para comparar los objetos, 
no si son iguales, sino si en realidad son el mismo objeto, 
con la misma ubicación de memoria:

is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y

Operadores de membresía
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
"""

#Listas en python
#Las listas se utilizan para almacenar varios elementos en una sola variable.
"""
Colecciones de Python (matrices)
Hay cuatro tipos de datos de recopilación en el lenguaje de programación Python:

La lista es una colección ordenada y modificable. Permite miembros duplicados.
Tuple es una colección ordenada e inmutable. Permite miembros duplicados.
Conjunto es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""

thislist = ["apple", "banana", "cherry"]
thislist1 = list("Mauricio ", "Quintero ", "Martinez", 25 ) # Se puede crear con costructor
print(thislist)
print(type(thislist)) #tipo de dato de thislist
print(thislist[-1]) #Imprime el último elemento de la lista

#Valida si un valor existe
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant" #Cambiar valor de la posicion 1
thislist.insert(2, "watermelon") #Inserta sandía en la tercer posicion
thislist.append("orange") #Agrega al final de la lista
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #agregar elementos de otra lista a la lista actual
print(thislist)
thislist.remove("banana") #Elimina elemento especificado
thislist.pop(1) #Elimina el indice especificado
thislist.pop() #Si no especifica indice, elimina el ultimo elemento
del thislist[0] #Tambien elimina el indice especificado
del thislist #Tambien puede eliminar la lista por completo
thislist.clear() #Vacía la lista, La lista aún permanece, pero no tiene contenido.
#Recorrer la lista
for x in thislist:
  print(x)
#Recorrer con un while
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#######
[print(x) for x in thislist] #Looping Using List Comprehension
#######

##Basado en la lista thislist, 
# desea una nueva lista que contenga solo las frutas con la letra "a" en el nombre.

#Sin comprensión de lista,
newlist = []

for x in thislist:
  if "a" in x:
    newlist.append(x)

print(newlist) 

#Con la comprensión de listas puedes hacer todo eso con solo una línea de código:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Sintaxis: newlist = [expression for item in iterable if condition == True]

#Iterable
#Puede usar la range()función para crear un iterable:
newlist = [x for x in range(10)]
#output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = [x for x in range(10) if x < 5]
#output: [0, 1, 2, 3, 4]
newlist = [x.upper() for x in fruits] #Establezca los valores en la nueva lista en mayúsculas:


#Python - Ordenar listas
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #ordenará la lista de forma alfanumérica, ascendente
thislist.sort(reverse = True) #Para ordenar de forma descendente

#Ordene la lista según lo cerca que esté el número de 50:
def myfunc(n):
  return abs(n - 50) #abs propio de py

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Copiar lista
mylist = thislist.copy() #Python - Copiar listas
mylist = list(thislist) #Tambien se puede copiar asi

#TUPLAS - Una tupla es una colección ordenada e inmutable
thistuple = ("apple", "banana", "cherry") #A diferencia de las listas,se escriben con ()
print(thistuple)
print(thistuple[1]) #Acceso a tuplas

#Cambiar valores en tupla, las tuplas son inmutables
#Puede convertir la tupla en una lista, cambiar la lista y volver a convertir la lista en una tupla.
x = ("apple", "banana", "cherry") 
y = list(x) 
y[1] = "kiwi"
x = tuple(y)

#Agregar tupla a tupla
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

#Recorrido con bucle for
for i in range(len(thistuple)):
  print(thistuple[i])

#Conjuntos de python
#NO puede cambiar los elementos pero si se pueden agregar/eliminar
##Un conjunto es una colección desordenada , inmutable*, no indexada y no se puede repetir elementos##
thisset = {"apple", "banana", "cherry"} #Crear un conjunto
print(thisset)
thisset.add("orange") #Agregar elementos
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #agregar elementos de otro conjunto al conjunto actual
mylist = ["kiwi", "orange"] #lista
thisset.update(mylist) #Puede agregar cualquier iterable
thisset.remove("banana") #Eliminar elemento del conjunto - Genera error
thisset.discard("banana") #Eliminar elemento del conjunto, NO genera error
thisset.clear() #Vacía el conjunto
del thisset #Elimina el conjunto
for x in thisset: #Solo se puede recorrer con ciclo for
  print(x)

#Python - Unir conjuntos
#Union
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #devuelve un nuevo conjunto con todos los elementos de ambos conjuntos:
set1.update(set2) #inserta los elementos en set2 en set1:
#Interseccion
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) #mantendrá solo los elementos que están presentes en ambos conjuntos.
z = x.intersection(y) #Devuelve un conjunto que contiene los elementos que existen tanto en conjunto xcomo en conjunto y
#Diferencia simetrica
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) #Conservar todo, pero NO los duplicados
z = x.symmetric_difference(y) #devolverá un nuevo conjunto, que contiene solo los elementos que NO están presentes en ambos conjuntos.


#DICCIONARIO
#Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.
#Un diccionario es una colección ordenada*, modificable y que no admite duplicados.
thisdict = { #Crear diccionario
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"]) #se puede hacer referencia a ellos mediante el nombre de la clave.
x = thisdict["model"]
x = thisdict.get("model") #Dará el mismo resultado
x = thisdict.keys() #Obtenga una lista de las claves
thisdict["color"] = "white"
print(x) #X es una vista del diccionario, si cambia alguna key tambien lo hara x
y = thisdict.values() #Obtenga una lista de los valores
thisdict["color"] = "yellow" #y es una vista del diccionario, si cambia algun valor tambien lo hara y
z = thisdict.items() #Obtener una lista de los pares clave:valor
if "model" in thisdict: #comprobar si existe la clave
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
thisdict["year"] = 2018 #Cambiar valor
thisdict.update({"year": 2020}) #ctualizará el diccionario con los elementos del argumento dado. Si el artículo no existe, se agregará.
thisdict["color"] = "red" #adicion de elementos
thisdict.pop("model") #elimina el elemento con el nombre de clave especificado
thisdict.popitem() #elimina el último elemento insertado 
del thisdict["model"] #elimina el elemento con el nombre de clave especificado
del thisdict #Elimina el diccionario por completo
thisdict.clear() #vacia el diccionario
for x in thisdict: #el valor devuelto son las claves del diccionario
  print(x)
for x in thisdict: #Imprime todos los valores en el diccionario, uno por uno:
  print(thisdict[x])
for x in thisdict.values(): #método para devolver valores de un diccionario:
  print(x)
for x in thisdict.keys(): #método para devolver las claves de un diccionario
  print(x)
for x, y in thisdict.items(): #Recorra las claves y los valores
  print(x, y)
mydict = thisdict.copy() #copia de un diccionario
mydict = dict(thisdict) #Haz una copia de un diccionario
myfamily = { #diccionario que contenga tres diccionarios
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
child1 = { #Cree tres diccionarios, luego cree un diccionario que contenga los otros tres diccionarios
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}