# -*- coding: utf-8 -*-
__author__ = 'Richard'

# Defino la varible 'futbolistas' como un diccionario. No es necesario declarar que tipo de dato es
futbolistas = dict()

futbolistas = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}

# Recorrer un diccionario, imprimiendo su clave-valor
for k,v in futbolistas.items():
    print "%s -> %s" %(k,v)

# Vemos cuantos elementos tiene nuestro diccionario
numElem = len(futbolistas)
print "\nNumero de elementos del diccionario len(futbolistas) = %i" %numElem

# Imprimimos una lista con las claves del diccionario
keys = futbolistas.keys();
print "\nClaves del diccionario futbolistas.keys(): \n%s" %keys

# Imprimimos en una lista los valores del diccionario
values = futbolistas.values()
print "\nValores del diccionario futbolistas.values(): \n%s" %values

# Obtenemos el valor de un elemento dada su clave
elem = futbolistas.get(6)
print "\nObtenemos el valor cuya clave es '6' futbolistas.get(6): %s" %elem

# Insertamos un elemento en el array. Si la clave ya existe no inserta el elemento
elem2 = futbolistas.setdefault(10,'Cesc')
print "\nInsertamos un elemento en el diccionario. Si la clave existe no lo inserta" \
      "\nfutbolistas.setdefault(10,'Cesc'): %s" %elem2

# Añadimos un nuevo elemento a la lista
futbolistas[22] = 'Navas'
print "\nDiccionario tras añadir un elemento: futbolistas[22] = 'Navas' \n%s" %futbolistas

# Eliminamos un elemento del diccionario dada su clave
futbolistas.pop(22)
print "\nDiccionario tras eliminar un elemento: futbolistas.pop(22) \n%s" %futbolistas

# Hacemos una copia del diccionario
futbolistasCopy = futbolistas.copy();
print "\nRealizamos una copia del diccionario futbolistasCopy=futbolistas.copy(): \n%s" %futbolistas

# Eliminamos los elementos de un diccionario
futbolistasCopy.clear()
print "\nEliminamos los elementos de un diccionario futbolistasCopy.clear(): %s" %futbolistasCopy

# Creamos un diccionario a partir de una lista con las claves
keys = ['nombre', 'apellidos', 'edad']
dictList = dict.fromkeys(keys, 'nada')
print "\nCreamos un diccionario a partir de una lista dictList = dict.fromkeys(keys, 'nada'): \n%s" %dictList

# Comprobamos si existe o no una clave
exit2 = futbolistas.has_key(2)
exit8 = futbolistas.has_key(8)
print "\nComprobamos si existen los elementos 2 y 8 \n\tfutbolistas.has_key(2) = %s " \
      "\n\tfutbolistas.has_key(8) = %s" %(exit2,exit8)

# Devolvemos los elementos del diccionario en tuplas
tuplas = futbolistas.items()
print "\nPasamos el diccionario a tuplas con clave-valor: tuplas = futbolistas.items() \n%s" %tuplas

# Mergeamos dos diccionarios
suplentes = {
    4:'Marchena', 9:'Torres', 12:'Valdes',
    13:'Mata' , 17:'Arbeloa', 19:'Llorente',
    20:'Javi Martinez', 21:'Silva', 23:'Reina'
}

futbolistas.update(suplentes)
print "\nAñadimos los elementos de un diccionario a otro futbolistas.update(suplentes): \n%s" %futbolistas
