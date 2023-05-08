import sys, re

if __name__ == '__main__':
    text = sys.stdin.read()

    words = [str(x).lower() for x in re.split('[.?!,-:;]*\\s', text) if x]
    count_dictionary = {x: words.count(x) for x in words}
    keys = list(count_dictionary.keys())
    keys.sort()
    sorted_count_dictionary = {k: count_dictionary[k] for k in keys}

    for k, v in sorted_count_dictionary.items():
        print('{}: {}'.format(k, v))