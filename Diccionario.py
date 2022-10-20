d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
  
}
#print(d1)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}

# mostar algun elemento del diccionario 

#print(d1['Nombre'])     #Sara



#Los diccionarios se pueden iterar de manera muy similar a las listas u otras estructuras de datos. Para imprimir los key.

# Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)
#Nombre Laura
# Edad 27
#Documento 1003882
