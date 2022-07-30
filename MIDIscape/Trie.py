

def luoTrie(x):
    Nuotit = x * 14
    lista = [[0 for _ in range(Nuotit)] for _ in range(Nuotit)]
    return lista

def lisaaIntervalli(x,y, lista):
    lista[x][y] += 1
    