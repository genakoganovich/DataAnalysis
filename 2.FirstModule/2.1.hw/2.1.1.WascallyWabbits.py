if __name__ == '__main__':
    n, k = map(int, input().split())

    f0 = f1 = 1
    for i in range(2, n):
        f0, f1 = f1, f0 * k + f1

    print(f1)
