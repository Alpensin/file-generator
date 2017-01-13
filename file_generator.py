import time

start = time.perf_counter()
def file_generator(size, dimension, bytes_in_kilobyte = 1024):
    """
    file_generator(size, dimension = 'MB', bytes_in_kilobyte = 1000)

    Create file with --size-- you set and with --dimension-- you set.

    bytes_in_kilobyte = 1024:
    List of dimensions: {"B" : 1, "KB" : 2**10, "MB" : 2**20, "GB" : 2**30, "TB" : 2**40}

    bytes_in_kilobyte = 1000:
    List of dimensions: {"B" : 1, "KB" : 10**3, "MB" : 10**6, "GB" : 10**9, "TB" : 10**12}
    """
    if bytes_in_kilobyte == 1000:
        suffixes = {"B" : 1, "KB" : 10**3, "MB" : 10**6, "GB" : 10**9, "TB" : 10**12}
    elif bytes_in_kilobyte == 1024:
        suffixes = {"B": 1, "KB": 2 ** 10, "MB": 2 ** 20, "GB": 2 ** 30, "TB": 2 ** 40}
    else:
        raise ValueError("Значение должно быть 1000 или 1024!")

    with open("%s%s.test" % (size, dimension), 'w+b') as out:
        filesize = size*suffixes.get(dimension)
        # for i in range(5):
        #     out.write(b"\0"*filesize)
        out.seek(filesize-1)
        out.write(b"\0")

file_generator(50, "GB")
end = time.perf_counter()
print("время выполнения %s" % (end-start))
