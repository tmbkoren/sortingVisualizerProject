import tkinter as tk
import random
from visualizer import draw_data
from sortingAlgo import bubble_sort, merge_sort, quick_sort, radix_sort
import threading


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
        arr = generateRandomArray(arrLength.get(), int(minVal.get()), int(maxVal.get())).copy()
        print('Array: ', arr)
        printValues(window, arr)

    tk.Button(window, text="Generate!", command=generateButtonHandler).pack()

    # Function to handle the click event of the 'sort' button, not functional yet

    def startSorting():
        def bubbleSortHandler():
            print('Bubble sort handler... ')
            bubble_sort(arr.copy())
        def mergeSortHandler():
            merge_sort(arr.copy())
        def quickSortHandler():
            quick_sort(arr.copy())
        def radixSortHandler():
            radix_sort(arr.copy())

        t1, t2, t3, t4 = None, None, None, None

        if bubbleSortBool.get():
            t1 = threading.Thread(target=bubbleSortHandler)
        if mergeSortBool.get():
            t2 = threading.Thread(target=mergeSortHandler)
        if quickSortBool.get():
            t3 = threading.Thread(target=quickSortHandler)
        if radixSortBool.get():
            t4 = threading.Thread(target=radixSortHandler)

        if t1:
            t1.start()
        if t2:
            t2.start()
        if t3:
            t3.start()
        if t4:
            t4.start()

    tk.Button(window, text="Sort!", command=startSorting).pack()
    window.mainloop()


if __name__ == "__main__":
    main()
