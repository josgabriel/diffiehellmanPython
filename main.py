import random

def potencia(base, expoente):
    aux = base
    for i in range (1, expoente):
        aux = aux * base
    return aux

primo = int(input('digite um número primo: '))
inteiro = int(input('digite um número inteiro: '))

numAlice = random.randint(1, 1000)
numBob = random.randint(1, 1000)

pubAlice = potencia(inteiro, numAlice) % primo
pubBob= potencia(inteiro, numBob) % primo

secAlice = potencia(pubBob, numAlice) % primo
secBob = potencia(pubAlice, numBob) % primo

if secAlice == secBob:
    print('\na chave secreta é:', secAlice)
else:
    print('\nhouve um erro')

print(f'chave pública de Alice: {pubAlice}')
print(f'chave pública de Bob: {pubBob}')
