import tkinter as tk
import random
from visualizer import draw_data
from sortingAlgo import bubble_sort, merge_sort, quick_sort, radix_sort
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

    bubbleSortBool = tk.IntVar()
    mergeSortBool = tk.IntVar()
    quickSortBool = tk.IntVar()
    radixSortBool = tk.IntVar()
    tk.Checkbutton(window, text="Bubble Sort", variable=bubbleSortBool).pack()
    tk.Checkbutton(window, text="Merge Sort", variable=mergeSortBool).pack()
    tk.Checkbutton(window, text="Quick Sort", variable=quickSortBool).pack()
    tk.Checkbutton(window, text="Radix Sort", variable=radixSortBool).pack()

    arrLength = tk.IntVar()
    minVal = tk.StringVar()
    maxVal = tk.StringVar()

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
                    quickSortBool.get(), radixSortBool.get()]
        processes = []
        
        for i, v in enumerate(selected):
            if v == 1:
                if i == 0:
                    print('Bubble sort selected')
                    p = multiprocessing.Process(target=bubble_sort, args=(arr, draw_data, 0.1))
                    processes.append(p)
                elif i == 1:
                    print('Merge sort selected')
                    p = multiprocessing.Process(target=merge_sort, args=(arr, draw_data, 0.1))
                    processes.append(p)
                elif i == 2:
                    print('Quick sort selected')
                    p = multiprocessing.Process(target=quick_sort, args=(arr, draw_data, 0.1))
                    processes.append(p)
                elif i == 3:
                    print('Radix sort selected')
                    p = multiprocessing.Process(target=radix_sort, args=(arr, draw_data, 0.1))
                    processes.append(p)
        
        for p in processes:
            p.start()

    tk.Button(window, text="Sort!", command=startSorting).pack()
    window.mainloop()


if __name__ == "__main__":
    main()
