import json
import os
import matplotlib.pyplot as plt
import numpy as np


def save_data(data: dict, path: str):
    cwd = os.getcwd()
    cwd += "/json" + path

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


# TODO: arreglar nombres de las soluciones para plotear test cases

def plot_test_results(number_of_tests, test_file, function_name, title, color='skyblue'):
    cwd = os.getcwd()
    cwd += "/json/"

    save_b = []
    with open(cwd+f'{test_file}.json', "r") as read_it:
        save_b = json.load(read_it)

    et_b = [save_b[i]['elapsed_time'] for i in range(number_of_tests)]
    sum_b = 0

    save_s = []
    with open(cwd+f'tests/{function_name}.json', "r") as read_it:
        save_s = json.load(read_it)

    et_s = [save_s[i]['elapsed_time'] for i in range(number_of_tests)]
    match_s = [save_s[i]['matches'] for i in range(number_of_tests)]
    sum_s = 0

    solutions = {0: [et_b, None, 'Backtrack', 'orange', sum_b],
                 1: [et_s, match_s, title, color, sum_s]}

    # plotting the points
    for i in range(len(solutions)):
        for j in range(number_of_tests):
            et = solutions[i][0][j]
            solutions[i][4] += et
            plt.plot(j, et, marker='o',
                     color='red' if i > 0 and solutions[i][1][j] == False else solutions[i][3])

        if i > 0:
            plt.suptitle(
                f'Resultados obtenidos con la solución mediante {solutions[i][2]}')
            plt.title(
                f'Cantidad de tests fallidos: {len(list(filter(lambda x: x == False, match_s)))}')
        else:
            plt.title(
                f'Resultados obtenidos con la solución mediante {solutions[i][2]}')
        # naming the x axis
        plt.xlabel('Test')
        # naming the y axis
        plt.ylabel('Tiempo')

        plt.savefig(cwd+f"tests/plots/{solutions[i][2]}_results.png")
        plt.clf()


def comparative_plot(number_of_tests, test_file):
    cwd = os.getcwd()
    cwd += "/json/"

    save_b = []
    with open(cwd+f'{test_file}.json', "r") as read_it:
        save_b = json.load(read_it)
    sum_b = np.sum([save_b[i]['elapsed_time'] for i in range(number_of_tests)])

    save_lp = []
    with open(cwd+f'tests/linear_prog_sol.json', "r") as read_it:
        save_lp = json.load(read_it)
    sum_lp = np.sum([save_lp[i]['elapsed_time']
                    for i in range(number_of_tests)])

    save_ga = []
    with open(cwd+f'tests/genetic_algorithm.json', "r") as read_it:
        save_ga = json.load(read_it)
    sum_ga = np.sum([save_ga[i]['elapsed_time']
                    for i in range(number_of_tests)])

    save_bma = []
    with open(cwd+f'tests/bellman_ford_mis.json', "r") as read_it:
        save_bma = json.load(read_it)
    sum_bma = np.sum([save_bma[i]['elapsed_time']
                     for i in range(number_of_tests)])

    solutions = {0: ['Backtrack', 'orange', sum_b],
                 1: ['Prog. Lineal', 'lightgreen', sum_lp],
                 2: ['A. Genético', 'plum', sum_ga],
                 3: ['BMA', 'skyblue', sum_bma]}

    for i in range(len(solutions)):
        ar_mean = solutions[i][2] / number_of_tests

        x = solutions[i][0]
        y = ar_mean
        plt.bar(x, y, color=solutions[i][1],
                width=0.5)

        plt.text(x, y, f'{round(y, 4)}', ha='center')

        plt.title(
            f'Comparación del tiempo promedio que demoró cada algoritmo')
        # naming the x axis
        plt.xlabel('Algoritmo')
        # naming the y axis
        plt.ylabel('Tiempo promedio')

        plt.savefig(cwd+f"tests/plots/Bar_comparative_plot.png")
