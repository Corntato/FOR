n = int(input("Introduceți numărul de zile (n): "))
distantă_totală = 0
săritură_curentă = 7
for zi in range(1, n + 1):
    distantă_totală += săritură_curentă
    săritură_curentă *= 10

print("Cangurul a sărit în total", distantă_totală, "metri în primele", n, "zile.")
