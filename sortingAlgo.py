import time
import multiprocessing
# Bubble Sort

pause_event = multiprocessing.Event()


def bubble_sort(arr, draw_data=None, delay=0, pause_event=None, startTime=None):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                if draw_data:
                    draw_data(arr, ['red' if x == j else 'blue' for x in range(len(arr))], startTime=startTime)

            if pause_event:
                while pause_event.is_set():
                    time.sleep(0.1)

            time.sleep(delay)
    return arr

# Merge Sort


def merge_sort(arr, draw_data=None, delay=0, pause_event=None, startTime=None):
    print('Merge sorting... ')

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, draw_data, delay, pause_event, startTime=startTime)
        merge_sort(R, draw_data, delay, pause_event, startTime=startTime)

        i = j = k = 0

        # Merge the two halves
        while i < len(L) and j < len(R):
            if pause_event:
                while pause_event.is_set():
                    time.sleep(0.1)

            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

            if draw_data:
                draw_data(arr, ["green" for x in range(len(arr))], algo_num=1, startTime=startTime)
            time.sleep(delay)

        while i < len(L):
            if pause_event:
                while pause_event.is_set():
                    time.sleep(0.1)

            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            if pause_event:
                while pause_event.is_set():
                    time.sleep(0.1)  # Pause while the event is cleared

            arr[k] = R[j]
            j += 1
            k += 1

        if draw_data:
            draw_data(arr, ["green" for x in range(len(arr))], algo_num=1, startTime=startTime)

        time.sleep(delay)

    return arr

# Quick Sort


def quick_sort(arr, draw_data=None, delay=0, low=0, high=None, pause_event=None, startTime=None):
    print('Quick sorting... ')

    if pause_event:
        while pause_event.is_set():
            time.sleep(0.1)

    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high, draw_data, delay, pause_event, startTime=startTime)

        if pause_event:
            while pause_event.is_set():
                time.sleep(0.1)

        quick_sort(arr, draw_data, delay, low, pi - 1, pause_event=pause_event, startTime=startTime)
        quick_sort(arr, draw_data, delay, pi + 1, high, pause_event=pause_event, startTime=startTime)

    if pause_event:
        while pause_event.is_set():
            time.sleep(0.1)

    return arr


def partition(arr, low, high, draw_data=None, delay=0, pause_event=None, startTime=None):
    pivot = arr[high]
    i = low - 1

    if pause_event:
        while pause_event.is_set():
            time.sleep(0.1)

    for j in range(low, high):
        if pause_event:
            while pause_event.is_set():
                time.sleep(0.1)
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        if draw_data:
            draw_data(arr, ["green" if x == i or x ==
                      j else "blue" for x in range(len(arr))], algo_num=2, startTime=startTime)
        time.sleep(delay)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if pause_event:
        while pause_event.is_set():
            time.sleep(0.1)
    if draw_data:
        draw_data(arr, ["green" if x == i or x ==
                        j else "blue" for x in range(len(arr))], algo_num=2, startTime=startTime)
        time.sleep(delay)
    return i + 1

# Radix Sort


def radix_sort(arr, draw_data=None, delay=0, pause_event=None, startTime=None):
    print('Radix sorting... ')
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        if pause_event:
            while pause_event.is_set():
                time.sleep(0.1)  # pause the process while the pause event is set

        counting_sort(arr, exp, draw_data, delay, pause_event, startTime=startTime)  # pass pause to counting_sort also
        exp *= 10

    return arr


def counting_sort(arr, exp, draw_data=None, delay=0, pause_event=None, startTime=None):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    if pause_event:
        while pause_event.is_set():
            time.sleep(0.1)

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

        if draw_data:
            draw_data(arr, ["green" if x == i else "blue" for x in range(len(arr))], algo_num=3, startTime=startTime)

        if pause_event:
            while pause_event.is_set():
                time.sleep(0.1)  # pause here also during each counting step

        time.sleep(delay)

    for i in range(n):
        arr[i] = output[i]

    if draw_data:
        draw_data(arr, ["green" for x in range(len(arr))], algo_num=3, startTime=startTime)
