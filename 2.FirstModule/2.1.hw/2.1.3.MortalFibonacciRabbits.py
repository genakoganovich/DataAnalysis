def din_fib(n, m):
    lst = [0] * m
    a = lst[-2] = lst[-1] = b = 1
    for i in range(2, n):
        a, b = b, a + b - lst.pop(0)
        lst.append(a)
    return b


if __name__ == '__main__':
    print(din_fib(*map(int, input().split())))