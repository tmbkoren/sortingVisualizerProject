import matplotlib.pyplot as plt


def draw_data(arr, color_array):
    plt.clf()  # Clear the previous plot
    plt.xlabel(arr)
    plt.bar(range(len(arr)), arr, color=color_array, width=0.1)
    plt.pause(0.1)  # Pause for the animation


def visualize_sorting(algorithm, arr, delay=0.05):
    res = algorithm(arr, draw_data, delay)
    plt.show()
    return res
