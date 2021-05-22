def ari_prog(start, stop, step):
    while start < stop:
        yield start

        start += step


if __name__ == '__main__':  # pragma: no cover
    for i in ari_prog(0, 10, 2):
        print(i)
