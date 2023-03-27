Classe chamada "Contador" que tem uma variável "valor" e dois métodos "incrementar" e "zerar".

class Contador:
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial
    
    def incrementar(self):
        self.valor += 1
        
    def zerar(self):
        self.valor = 0




# criando objetos
contador1 = Contador()
contador2 = Contador(5)
contador3 = Contador(10)

# imprimindo os valores iniciais
print("Valor inicial do contador1:", contador1.valor)
print("Valor inicial do contador2:", contador2.valor)
print("Valor inicial do contador3:", contador3.valor)

# incrementando e imprimindo os novos valores
contador1.incrementar()
contador2.incrementar()
contador3.incrementar()
print("Valor após incrementar contador1:", contador1.valor)
print("Valor após incrementar contador2:", contador2.valor)
print("Valor após incrementar contador3:", contador3.valor)

# zerando e imprimindo os valores finais
contador1.zerar()
contador2.zerar()
contador3.zerar()
print("Valor final do contador1:", contador1.valor)
print("Valor final do contador2:", contador2.valor)
print("Valor final do contador3:", contador3.valor)

Valor inicial do contador1: 0
Valor inicial do contador2: 5
Valor inicial do contador3: 10
Valor após incrementar contador1: 1
Valor após incrementar contador2: 6
Valor após incrementar contador3: 11
Valor final do contador1: 0
Valor final do contador2: 0
Valor final do contador3: 0
