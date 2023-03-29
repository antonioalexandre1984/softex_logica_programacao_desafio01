def inverter_string(texto):
    return texto[::-1]

# Exemplo de uso:
texto = "hello world"
texto_invertido = inverter_string(texto)
print(f"O texto '{texto}' invertido é '{texto_invertido}'")


import re

def remover_caracteres(texto):
    return re.sub(r'[^\w\s]', '', texto)

# Exemplo de uso:
texto = "Hello, world! How are you?"
texto_sem_caracteres = remover_caracteres(texto)
print(f"O texto '{texto}' sem caracteres especiais é '{texto_sem_caracteres}'")
