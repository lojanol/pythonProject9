# definir una lista para almacenar los datos
libros=[]
# funcion para capturar los datos de un libro
def capturar_datos():
    nombre=input("nombre del libro:")
    categoria=input("categoria:")
    ano_publicacion=input("año de publicacion:")
    numero_paginas=input("numero de paginas:")
    autor=input("autor:")

    # crear un diccionario para el libro
    libro={
    "nombre":nombre,
    "catyegoria": categoria,
    "año_publicacion": ano_publicacion,
    "numero_paginas":numero_paginas,
    "autor":autor

    }
# guardar en la variable libros
capturar_datos()
# funcion para imprimir la lista de datos
def imprimir_libros():
 print(libros)