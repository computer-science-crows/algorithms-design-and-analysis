import json
import os
import matplotlib.pyplot as plt


def save_data(data: dict, path: str):
    cwd = os.getcwd()
    cwd += "/baseball/json" + path

    save = []

    try:
        with open(cwd, "r") as read_it:
            save = json.load(read_it)

        save.append(data)

        with open(cwd, "w") as write_it:
            json.dump(save, write_it)
    except:
        save.append(data)

        with open(cwd, "w") as write_it:
            json.dump(save, write_it)


def plot_test_results():
    cwd = os.getcwd()
    cwd += "/baseball/json/"

    save_b = []
    with open(cwd+'test_cases.json', "r") as read_it:
        save_b = json.load(read_it)

    et_b = [save_b[i]['elapsed_time'] for i in range(3000)]

    save_s = []
    with open(cwd+'tests/simplex_solution.json', "r") as read_it:
        save_s = json.load(read_it)

    save_h = []
    with open(cwd+'tests/hungarian_solution.json', "r") as read_it:
        save_h = json.load(read_it)

    # x axis values
    test_number = [i for i in range(3000)]

    # plotting line
    for i in range(3000):
        plt.plot(test_number, et_b, color='gray')

    # plotting the points
    for i in range(3000):
        fit = et_b[i]
        plt.plot(i, fit, marker='o', color='limegreen')

    # plt.plot(i, fit, marker='o',
    #             color='red' if save_b[i]['matches'] else 'limegreen')

    # # naming the x axis
    # plt.xlabel('Test')
    # # naming the y axis
    # plt.ylabel('Fitness de la solución final')

    # giving a title to my graph
    plt.title('Resultados obtenidos')

    # plt.xticks(np.arange(0, 50, 1.0))

    # function to show the plot
    plt.savefig(cwd+"tests/Comparative_Results.png")


plot_test_results()
