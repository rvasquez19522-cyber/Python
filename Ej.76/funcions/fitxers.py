# funcions/fitxers.py

def gestionar_llista_compra():
    # Nombre del archivo
    archivo = 'llista_compra.txt'
    
    # Función para agregar un artículo
    def agregar_articulo(articulo):
        with open(archivo, 'a') as f:
            f.write(articulo + '\n')
        print(f'Artículo "{articulo}" añadido a la lista.')

    # Función para mostrar todos los artículos
    def mostrar_lista():
        try:
            with open(archivo, 'r') as f:
                lista = f.readlines()
            print("Lista de la compra:")
            for articulo in lista:
                print(articulo.strip())
        except FileNotFoundError:
            print("No hay lista guardada.")
    
    # Función para borrar un artículo
    def borrar_articulo(articulo):
        try:
            with open(archivo, 'r') as f:
                lista = f.readlines()
            lista = [item for item in lista if item.strip() != articulo]
            with open(archivo, 'w') as f:
                f.writelines(lista)
            print(f'Artículo "{articulo}" borrado de la lista.')
        except FileNotFoundError:
            print("No hay lista guardada.")
    
    # Ejemplo de uso
    agregar_articulo("Leche")
    agregar_articulo("Pan")
    mostrar_lista()
    borrar_articulo("Leche")
    mostrar_lista()
