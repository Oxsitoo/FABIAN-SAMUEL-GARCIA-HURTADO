import re

# Ruta del archivo de texto
ruta_archivo = 'italiano.txt'

# Abrimos y leemos el contenido
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Expresiones regulares corregidas
expresiones = {
    # Flotantes: con o sin signo, número con punto decimal
    'flotantes': re.findall(r'[-+]?\d+\.\d+', texto),

    # Enteros: con o sin signo, sin punto decimal (pero que no formen parte de un flotante)
    'enteros': re.findall(r'(?<![\d.])[-+]?\d+(?!\.\d)', texto),

    # Listas: cualquier cosa dentro de corchetes, no muy codicioso
    'listas': re.findall(r'\[(.*?)\]', texto),

    # Palabras: incluyendo tildes y ñ, tanto mayúsculas como minúsculas
    'palabras': re.findall(r'\b[\wáéíóúÁÉÍÓÚñÑ]+\b', texto)
}

# Mostrar resultados
for tipo, resultados in expresiones.items():
    print(f"\n{tipo.capitalize()} encontrados:")
    for resultado in resultados:
        print(f" - {resultado}")