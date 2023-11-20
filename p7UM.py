for num in range(100, 600):
    s = num // 100
    z = (num // 10) % 10
    u = num % 10
    if s < z < u and s + z + u == 18:
        print(num)
