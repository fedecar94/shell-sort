def shell_sort(array: list):
    size = len(array)

    for gap in range(size // 2, 0, -1):
        for i in range(gap, size):
            if array[i] < array[i - gap]:
                array[i], array[i - gap] = array[i - gap], array[i]


if __name__ == '__main__':
    import random

    randomlist = [random.randint(1, 30) for x in range(0, 10)]

    print(randomlist)
    shell_sort(randomlist)
    print(randomlist)
