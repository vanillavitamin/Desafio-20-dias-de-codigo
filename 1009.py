nome = input()
salario = float(input())
vendas = float(input())

montante = (vendas * 0.15) + salario
print(f"TOTAL = R$ {montante:.2f}")
