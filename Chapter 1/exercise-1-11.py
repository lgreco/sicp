def f(n):
    if n < 3:
        result = n
    else:
        result = f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)
    return result

def f_iter(n):
    if n < 3:
        return n
    f0, f1, f2 = 0, 1, 2  # Corresponds to f(0), f(1), f(2)
    for i in range(3, n + 1):
        current = f2 + 2 * f1 + 3 * f0
        f0, f1, f2 = f1, f2, current
    return f2

test_n = 20
print(f(test_n))
print(f_iter(test_n))