import tkinter as tk
import random
from visualizer import visualize_sorting, draw_data
from sortingAlgo import bubble_sort, merge_sort, quick_sort, radix_sort, pause_event
from searchAlgo import linear_search
import multiprocessing


def printValues(window, values):
    print('Values: ', values)
    tk.Label(window, text=values, wraplength=600).pack()


def generateRandomArray(length, minVal, maxVal):
    temp = [random.randint(minVal, maxVal) for _ in range(length)]
    print('Temp: ', temp)
    return temp


arr = []


def sortingUI(window):
    print('Sorting UI')
    subwindow = tk.Toplevel(window)
    subwindow.title("Sorting Algorithm Visualizer")
    subwindow.geometry("800x600")

    bubbleSortBool = tk.IntVar(value=1)
    mergeSortBool = tk.IntVar(value=1)
    quickSortBool = tk.IntVar(value=1)
    radixSortBool = tk.IntVar(value=1)
    tk.Checkbutton(subwindow, text="Bubble Sort", variable=bubbleSortBool).pack()
    tk.Checkbutton(subwindow, text="Merge Sort", variable=mergeSortBool).pack()
    tk.Checkbutton(subwindow, text="Quick Sort", variable=quickSortBool).pack()
    tk.Checkbutton(subwindow, text="Radix Sort", variable=radixSortBool).pack()

    speed = tk.IntVar(value=100)

    tk.Label(subwindow, text="Select delay(ms) between steps: ").pack()
    tk.Scale(subwindow, from_=50, to=1000, resolution=1,
             orient=tk.HORIZONTAL, length=400, variable=speed).pack()

    arrLength = tk.IntVar(value=15)
    minVal = tk.StringVar(value=1)
    maxVal = tk.StringVar(value=40)

    tk.Label(subwindow, text="Select array length: ").pack()
    tk.Scale(subwindow, from_=1, to=100,
             orient=tk.HORIZONTAL, length=400, variable=arrLength).pack()
    tk.Label(subwindow, text="Select minimum value: ").pack()
    tk.Entry(subwindow, textvariable=minVal).pack()
    tk.Label(subwindow, text="Select maximum value: ").pack()
    tk.Entry(subwindow, textvariable=maxVal).pack()

    def generateButtonHandler():
        global arr
        arr = generateRandomArray(arrLength.get(), int(
            minVal.get()), int(maxVal.get())).copy()
        print('Array: ', arr)
        printValues(subwindow, arr)

    tk.Button(subwindow, text="Generate!", command=generateButtonHandler).pack()

    # Function to handle the click event of the 'sort' button, not functional yet

    def startSorting():
        selected = [bubbleSortBool.get(), mergeSortBool.get(),
                    quickSortBool.get(), radixSortBool.get()]
        processes = []
        delay = speed.get()/1000

        for i, v in enumerate(selected):
            if v == 1:
                if i == 0:
                    print('Bubble sort selected')
                    p = multiprocessing.Process(
                        # target=visualize_sorting, args=(bubble_sort, arr, delay))
                        target=visualize_sorting, args=(bubble_sort, arr, delay, pause_event))
                    processes.append(p)
                elif i == 1:
                    print('Merge sort selected')
                    p = multiprocessing.Process(
                        target=visualize_sorting, args=(merge_sort, arr, delay, pause_event))
                    processes.append(p)
                elif i == 2:
                    print('Quick sort selected')
                    p = multiprocessing.Process(
                        target=visualize_sorting, args=(quick_sort, arr, delay, pause_event))
                    processes.append(p)
                elif i == 3:
                    print('Radix sort selected')
                    p = multiprocessing.Process(
                        target=visualize_sorting, args=(radix_sort, arr, delay, pause_event))
                    processes.append(p)

        for p in processes:
            p.start()

    tk.Button(subwindow, text="Sort!", command=startSorting).pack()


    def pause():
        pause_event.set() # Pauses all processes

    def resume():
        pause_event.clear()  # Resumes all processes

    # Pause button
    tk.Button(subwindow, text="Pause", command=pause).pack()

    # Resume button
    tk.Button(subwindow, text="Resume", command=resume).pack()


def searchUI(window):
    subwindow = tk.Toplevel(window)
    subwindow.title("Linear Search Algorithm Visualizer")
    subwindow.geometry("800x600")

    speed = tk.IntVar(value=100)

    tk.Label(subwindow, text="Select delay(ms) between steps: ").pack()
    tk.Scale(subwindow, from_=50, to=1000, resolution=1,
             orient=tk.HORIZONTAL, length=400, variable=speed).pack()

    minVal = tk.StringVar(value=1)
    maxVal = tk.StringVar(value=40)


    arrLength = tk.IntVar(value=15)
    tk.Label(subwindow, text="Select array length: ").pack()
    arrLenScale = tk.Scale(subwindow, from_=1, to=100,
             orient=tk.HORIZONTAL, length=400, variable=arrLength)
    arrLenScale.pack()
    tk.Label(subwindow, text="Select minimum value: ").pack()
    tk.Entry(subwindow, textvariable=minVal).pack()
    tk.Label(subwindow, text="Select maximum value: ").pack()
    tk.Entry(subwindow, textvariable=maxVal).pack()

    def generateButtonHandler():
        global arr
        arr = generateRandomArray(arrLength.get(), int(
            minVal.get()), int(maxVal.get())).copy()
        print('Array: ', arr)
        printValues(subwindow, arr)

    tk.Button(subwindow, text="Generate!", command=generateButtonHandler).pack()

    tk.Label(subwindow, text="Select the value to search: ").pack()
    searchVal = tk.StringVar(value=1)
    tk.Entry(subwindow, textvariable=searchVal).pack()

    # def handleLinearSearch(arr, delay, target, pause_event):
    #     res = linear_search(
    #         arr,
    #         delay,
    #         target,
    #         pause_event
    #     )

    #     print(f'Search result: {res}')
    #     tk.Label(subwindow, text=f'Search result: {res}').pack()

    def startSearching():

        search_pause_event = multiprocessing.Event()

        p = multiprocessing.Process(target=linear_search, args=(
            arr, speed.get()/1000, int(searchVal.get()), search_pause_event))
        p.start()

        def pause():
            search_pause_event.set() # Pauses all processes

        def resume():
            search_pause_event.clear()  # Resumes all processes

        # Pause button
        tk.Button(subwindow, text="Pause", command=pause).pack()

        # Resume button
        tk.Button(subwindow, text="Resume", command=resume).pack()

    tk.Button(subwindow, text="Search!", command=startSearching).pack()

    print(f'Array: {arr}, arrLength: {arrLength.get()}, minVal: {minVal.get()}, maxVal: {maxVal.get()}')



def main():
    # UI declaration
    window = tk.Tk()
    window.title("Sorting Algorithm Visualizer")
    window.geometry("300x100")

    tk.Button(window, text="Sorting mode", command=lambda: sortingUI(window)).pack()
    tk.Button(window, text="Searching mode", command=lambda: searchUI(window)).pack()

    window.mainloop()


if __name__ == "__main__":
    main()
