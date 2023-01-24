n = int(input('Digite a quantidade de números da sua lista: '))
t = list(map(int, input('Agora digite os números da lista: ').split()))[:n]

for j in range(1, n):
    chave = t[j]
    i = j - 1

    while i >= 0 and t[i] > chave:
        t[i + 1] = t[i]
        i = i - 1
        t[i + 1] = chave

print(*t[:8])
print('Aí está!')
