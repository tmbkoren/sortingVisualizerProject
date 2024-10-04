#           Linear search algo.
import time
#import tkinter as tk
import matplotlib.pyplot as plt
import multiprocessing

search_pause_event = multiprocessing.Event()

def draw_data(arr, color_array, delay=0.05, algo_num=0, startTime=0):
    plt.clf()  # Clear the previous plot
    # plt.xlabel(arr)
    plt.title(f'Linear Search Algo - Time {time.time() - startTime:.2f}s')
    plt.bar(range(len(arr)), arr, color=color_array, width=0.1)
    wnd = plt.get_current_fig_manager()
    # Set the window resolution and position
    wnd.window.wm_geometry(f"600x400+40+40")
    plt.pause(delay)  # Pause for the animation


def linear_search(arr, delay=0, target=1, pause_event=None, subwindow=None):
    startTime = time.time()
    print(pause_event)
    for index in range(len(arr)):

        if pause_event:
            while pause_event.is_set():
                time.sleep(0.1)

        if draw_data:
            draw_data(arr, ['red' if x == index else 'blue' for x in range(len(arr))], delay, startTime=startTime)

        if arr[index] == target:
            if draw_data:
                draw_data(arr, ['green' if x == index else 'blue' for x in range(len(arr))], startTime=startTime)
            #tk.Label(subwindow, text=f'Search result: {index}').pack()
            print(f'Search result: {index}')
            return index

    if draw_data:
        draw_data(arr, ['blue' for x in range(len(arr))])

    #tk.Label(subwindow, text=f'Not found').pack()
    print('Not found')
    return -1
