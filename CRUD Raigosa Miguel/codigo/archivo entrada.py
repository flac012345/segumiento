import os

def convertir_a_mayusculas():
    # Ruta completa del archivo de entrada
    archivo_entrada = r"C:\Users\sala2.akademos\Documents\lenguajes de programacion\CRUD Raigosa Miguel\codigo\archivo_entrada.txt"
    # Nombre del archivo de salida
    archivo_salida = os.path.join(os.path.dirname(archivo_entrada), 'salida.txt')
    
    try:
        # Abrir el archivo de entrada en modo lectura
        with open(archivo_entrada, 'r', encoding='utf-8') as infile:
            # Leer el contenido del archivo
            contenido = infile.read()
        
        # Convertir el contenido a mayúsculas
        contenido_mayusculas = contenido.upper()
        
        # Abrir el archivo de salida en modo escritura
        with open(archivo_salida, 'w', encoding='utf-8') as outfile:
            # Escribir el contenido en mayúsculas en el archivo de salida
            outfile.write(contenido_mayusculas)

        print(f"El contenido de '{archivo_entrada}' ha sido escrito en '{archivo_salida}' en mayúsculas.")

    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no se encuentra.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Llamar a la función
convertir_a_mayusculas()
