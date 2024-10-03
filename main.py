import tkinter as tk
import random
from visualizer import visualize_sorting
from sortingAlgo import bubble_sort, merge_sort, quick_sort, radix_sort, linear_search
import multiprocessing


def printValues(window, values):
    print('Values: ', values)
    tk.Label(window, text=values, wraplength=600).pack()


def generateRandomArray(length, minVal, maxVal):
    temp = [random.randint(minVal, maxVal) for _ in range(length)]
    print('Temp: ', temp)
    return temp


arr = []


def main():
    # UI declaration
    window = tk.Tk()
    window.title("Sorting Algorithm Visualizer")
    window.geometry("800x600")

    bubbleSortBool = tk.IntVar(value=1)
    mergeSortBool = tk.IntVar(value=1)
    quickSortBool = tk.IntVar(value=1)
    radixSortBool = tk.IntVar(value=1)
    linearAlgoBool = tk.IntVar(value=1)
    tk.Checkbutton(window, text="Bubble Sort", variable=bubbleSortBool).pack()
    tk.Checkbutton(window, text="Merge Sort", variable=mergeSortBool).pack()
    tk.Checkbutton(window, text="Quick Sort", variable=quickSortBool).pack()
    tk.Checkbutton(window, text="Radix Sort", variable=radixSortBool).pack()
    tk.Checkbutton(window, text="Linear Search", variable=linearAlgoBool).pack()

    speed = tk.IntVar(value=100)

    tk.Label(window, text="Select delay(ms) between steps: ").pack()
    tk.Scale(window, from_=50, to=1000, resolution=1,
             orient=tk.HORIZONTAL, length=400, variable=speed).pack()

    arrLength = tk.IntVar(value=15)
    minVal = tk.StringVar(value=1)
    maxVal = tk.StringVar(value=40)

    tk.Label(window, text="Select array length: ").pack()
    tk.Scale(window, from_=1, to=100,
             orient=tk.HORIZONTAL, length=400, variable=arrLength).pack()
    tk.Label(window, text="Select minimum value: ").pack()
    tk.Entry(window, textvariable=minVal).pack()
    tk.Label(window, text="Select maximum value: ").pack()
    tk.Entry(window, textvariable=maxVal).pack()

    # Function to handle the click event of the 'generate' button

    def generateButtonHandler():
        global arr
        arr = generateRandomArray(arrLength.get(), int(
            minVal.get()), int(maxVal.get())).copy()
        print('Array: ', arr)
        printValues(window, arr)

    tk.Button(window, text="Generate!", command=generateButtonHandler).pack()

    # Function to handle the click event of the 'sort' button, not functional yet

    def startSorting():
        selected = [bubbleSortBool.get(), mergeSortBool.get(),
                    quickSortBool.get(), radixSortBool.get(), linearAlgoBool.get()]
        processes = []
        delay = speed.get()/1000

        for i, v in enumerate(selected):
            if v == 1:
                if i == 0:
                    print('Bubble sort selected')
                    p = multiprocessing.Process(
                        target=visualize_sorting, args=(bubble_sort, arr, delay))
                    processes.append(p)
                elif i == 1:
                    print('Merge sort selected')
                    p = multiprocessing.Process(
                        target=visualize_sorting, args=(merge_sort, arr, delay))
                    processes.append(p)
                elif i == 2:
                    print('Quick sort selected')
                    p = multiprocessing.Process(
                        target=visualize_sorting, args=(quick_sort, arr, delay))
                    processes.append(p)
                elif i == 3:
                    print('Radix sort selected')
                    p = multiprocessing.Process(
                        target=visualize_sorting, args=(radix_sort, arr, delay))
                    processes.append(p)
                elif i == 4:
                    print('Linear search selected')
                    p = multiprocessing.Process(
                        target=visualize_sorting, args=(linear_search, arr, delay))
                    processes.append(p)

        for p in processes:
            p.start()

    tk.Button(window, text="Sort!", command=startSorting).pack()
    window.mainloop()


if __name__ == "__main__":
    main()
