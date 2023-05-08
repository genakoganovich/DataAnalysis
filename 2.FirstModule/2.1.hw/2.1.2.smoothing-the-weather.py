if __name__ == '__main__':
    n = int(input())
    seq_in = [float(x) for x in input().split()]
    seq_out = seq_in.copy()
    for i in range(1, n - 1):
        seq_out[i] = round((seq_in[i - 1] + seq_in[i] + seq_in[i + 1]) / 3, 10)

    seq_out = [str(x).rstrip('.0') for x in seq_out]
    print(*seq_out)