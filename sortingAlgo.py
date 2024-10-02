import time

# Bubble Sort


def bubble_sort(arr, draw_data=None, delay=0):
    print('Bubble sorting... ')
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if draw_data:
                draw_data(arr, ["green" if x == j or x == j +
                          1 else "blue" for x in range(len(arr))])
            time.sleep(delay)
    return arr

# Merge Sort


def merge_sort(arr, draw_data=None, delay=0):
    print('Merge sorting... ')
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, draw_data, delay)
        merge_sort(R, draw_data, delay)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            if draw_data:
                draw_data(arr, ["green" for x in range(len(arr))])
            time.sleep(delay)

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Quick Sort


def quick_sort(arr, draw_data=None, delay=0, low=0, high=None):
    print('Quick sorting... ')
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high, draw_data, delay)
        quick_sort(arr, draw_data, delay, low, pi - 1)
        quick_sort(arr, draw_data, delay, pi + 1, high)

    return arr


def partition(arr, low, high, draw_data=None, delay=0):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        if draw_data:
            draw_data(arr, ["green" if x == i or x ==
                      j else "blue" for x in range(len(arr))])
        time.sleep(delay)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Radix Sort


def radix_sort(arr, draw_data=None, delay=0):
    print('Radix sorting... ')
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp, draw_data, delay)
        exp *= 10

    return arr


def counting_sort(arr, exp, draw_data=None, delay=0):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
        if draw_data:
            draw_data(
                arr, ["green" if x == i else "blue" for x in range(len(arr))])
        time.sleep(delay)
