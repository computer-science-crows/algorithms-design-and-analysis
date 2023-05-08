import json
import os
import matplotlib.pyplot as plt


def save_data(data: dict, path: str):
    cwd = os.getcwd()
    cwd += "/corruption-strategy/json" + path

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

def plot_test_results():
    cwd = os.getcwd()
    cwd += "/corruption-strategy/json/"

    save_b = []
    with open(cwd+'test_cases.json', "r") as read_it:
        save_b = json.load(read_it)

    et_b = [save_b[i]['elapsed_time'] for i in range(3000)]
    sum_b = 0

    save_s = []
    with open(cwd+'tests/simplex_solution.json', "r") as read_it:
        save_s = json.load(read_it)

    et_s = [save_s[i]['elapsed_time'] for i in range(3000)]
    match_s = [save_s[i]['matches'] for i in range(3000)]
    sum_s = 0

    save_h = []

    with open(cwd+'tests/hungarian_solution.json', "r") as read_it:
        save_h = json.load(read_it)

    et_h = [save_h[i]['elapsed_time'] for i in range(3000)]
    match_h = [save_h[i]['matches'] for i in range(3000)]
    sum_h = 0

    solutions = {2: [et_b, None, 'Backtrack', 'limegreen', sum_b],
                 0: [et_h, match_h, 'Hungarian', 'aqua', sum_h],
                 1: [et_s, match_s, 'Simplex', 'orchid', sum_s]}

    # plotting the points
    for i in range(len(solutions)):
        for j in range(3000):
            et = solutions[i][0][j]
            solutions[i][4] += et
            plt.plot(j, et, marker='o',
                     color='red' if solutions[i][1] == False else solutions[i][3])
        plt.title(
            f'Resultados obtenidos con la solución mediante {solutions[i][2]}')

        # naming the x axis
        plt.xlabel('Test')
        # naming the y axis
        plt.ylabel('Tiempo')

        plt.savefig(cwd+f"tests/plots/{solutions[i][2]}_results.png")
        plt.clf()

    for i in range(len(solutions)):
        ar_mean = solutions[i][4] / 3000

        x = solutions[i][2]
        y = ar_mean
        plt.bar(x, y, color=solutions[i][3],
                width=0.4)

        plt.text(x, y, f'{round(y, 4)}', ha='center')

        plt.title(
            f'Comparación del tiempo promedio que demoró cada algoritmo')
        # naming the x axis
        plt.xlabel('Algoritmo')
        # naming the y axis
        plt.ylabel('Tiempo promedio')

        plt.savefig(cwd+f"tests/plots/Bar_comparative_plot.png")
