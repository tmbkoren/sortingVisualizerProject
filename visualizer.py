import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# algo_num: 0 for bubble sort, 1 for merge sort, 2 for quick sort, 3 for radix sort
algo_names = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort']

# coordinates for window for each algorithm, same order, format is 'x+y'
coords = ['20+40', '720+40', '20+420', '720+420']

def draw_data(arr, color_array, delay=0.05, algo_num=0):
    plt.clf()  # Clear the previous plot
    #plt.xlabel(arr)
    plt.title(algo_names[algo_num])
    plt.bar(range(len(arr)), arr, color=color_array, width=0.1)
    wnd = plt.get_current_fig_manager()
    # Set the window resolution and position
    wnd.window.wm_geometry(f"600x400+{coords[algo_num]}")
    plt.pause(delay)  # Pause for the animation


def visualize_sorting(algorithm, arr, delay=0.05):
    res = algorithm(arr, draw_data, delay)
    plt.show()
    return res
