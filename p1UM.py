n = int(input("Introduceți un număr întreg n: "))
f = 1
for i in range(1, n + 1):
    f *= i

# Afișăm rezultatul
print("Factorialul lui" , n , "este:", f)