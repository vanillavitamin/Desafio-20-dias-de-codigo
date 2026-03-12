linha1 = input().split()
codigo1 = int(linha1[0])
numeropecas1 = int(linha1[1])
valor1 = float(linha1[2])

linha2 = input().split()
codigo2 = int(linha2[0])
numeropecas2 = int(linha2[1])
valor2 = float(linha2[2])

total = numeropecas1 * valor1 + numeropecas2 * valor2
print(f"VALOR A PAGAR: R$ {total:.2f}")
