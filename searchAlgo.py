#           Linear search algo.
import time
import matplotlib.pyplot as plt

def draw_data(arr, color_array, delay=0.05, algo_num=0, startTime=0):
    plt.clf()  # Clear the previous plot
    # plt.xlabel(arr)
    plt.title(f'Linear Search Algo, current runtime: {time.time() - startTime:.2f}s')
    plt.bar(range(len(arr)), arr, color=color_array, width=0.1)
    wnd = plt.get_current_fig_manager()
    # Set the window resolution and position
    wnd.window.wm_geometry(f"600x400+40+40")
    plt.pause(delay)  # Pause for the animation


def linear_search(arr, delay=0, target=1):
    startTime = time.time()

    for index in range(len(arr)):
        if draw_data:
            draw_data(
                arr, ['red' if x == index else 'blue' for x in range(len(arr))], startTime=startTime)

        # bit useless but if there is delay
        if delay:
            time.sleep(delay)

        if arr[index] == target:
            if draw_data:
                draw_data(
                    arr, ['green' if x == index else 'blue' for x in range(len(arr))], startTime=startTime)
            return index

    if draw_data:
        draw_data(arr, ['blue' for x in range(len(arr))])
    return -1
