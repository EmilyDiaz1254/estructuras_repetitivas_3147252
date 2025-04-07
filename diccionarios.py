##Diccionarios:

#Son coleciones de datos
#Cada elemento de un diccionario
##Se puede dividir en dos partes:
# ##  1.clave: el valor del elemento
# ##  2.clave: el valor del elemento
## Ejemplo de diccionario:
## Para caracterizar un pais

pais={
    "nombre":"colombia",
    "capital":"Bogota",
    "idioma":"español",
    "poblacion":51,
    "superficie":1141748,
    "moneda":"peso colombiano",
    "ciudades":[
        "bogota",
        "medellin",
        "cali",
        "barranquilla",
        "cartagena"
    ]
}

#acceder a propiedades:
print("capital de colombia", pais["capital"])
print("Y se habla:" , pais["idioma"])
print("habitantes:" , pais["poblacion"])
print("y sus ciudades son")
for ciudad in pais ["ciudades"]:
    print(ciudad)