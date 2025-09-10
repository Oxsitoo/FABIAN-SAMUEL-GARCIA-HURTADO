import re

# Ruta del archivo de texto
ruta_archivo = 'espanol.txt'

# Abrimos y leemos el contenido
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Expresiones regulares
expresiones = {
    'enteros': re.findall(r'(?<![\w.])-?\b\d+\b(?!\.\d)', texto),
    'flotantes': re.findall(r'(?<!\w)-?\b\d+\.\d+\b', texto),
    'listas': re.findall(r'\[.*?\]', texto),
    'palabras': re.findall(r'\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b', texto)
}

# Mostrar resultados
for tipo, resultados in expresiones.items():
    print(f"\n{tipo.capitalize()} encontrados:")
    for resultado in resultados:
        print(f" - {resultado}")
