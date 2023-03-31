import json
import os
import time
from colored import fore, back, style

cwd = os.getcwd()
cwd += "/baseball/json"
# print(cwd)

t = [{"n": 2, "p": 3, "k": 6, "a": 9, "s": 4, "optimal_solution": 10},
     {"n": 1, "p": 3, "k": 6, "a": 9, "s": 4, "optimal_solution": 19}]
with open(cwd+"/test_cases.json", "w") as write_it:
    json.dump(t, write_it)


def function1(n, p, k, a, s):
    return 10


def function2(n, p, k, a, s):
    return 19


def tester(function):
    test_cases = {}
    with open(cwd+"/test_cases.json", "r") as read_it:
        test_cases = json.load(read_it)

    print(style.BOLD + f"Testing {function.__name__}" + style.RESET)
    print("-------------------------------------------")

    for index, tc in enumerate(test_cases):
        # print(tc)
        testing_data = {}

        start = time.time()
        testing_data["f_result"] = function(
            tc['n'], tc['p'], tc['k'], tc['a'], tc['s'])
        end = time.time()

        testing_data["elapsed_time"] = end - start

        testing_data["matches"] = False
        if testing_data["f_result"] == tc["optimal_solution"]:
            testing_data["matches"] = True

        # print(testing_data)

        try:
            prev_testing_data = []
            with open(cwd+f"/tests/{function.__name__}.json", "r") as read_it:
                prev_testing_data.append(json.load(read_it))

            if prev_testing_data[0] == None:
                prev_testing_data = testing_data
            else:
                prev_testing_data.append(testing_data)

            with open(cwd+f"/tests/{function.__name__}.json", "w") as write_it:
                json.dump(prev_testing_data, write_it)
        except:
            with open(cwd+f"/tests/{function.__name__}.json", "w") as write_it:
                json.dump(testing_data, write_it)

        print(f"Test case #{index + 1} -> " + back.RED + style.BOLD +
              "FAILED" + style.RESET if testing_data['matches'] == False else f"Test case #{index + 1} -> " + back.GREEN + style.BOLD +
              "SUCCESS" + style.RESET)
        print(f"  result: {testing_data['f_result']}")
        print(f"  elapsed time: {testing_data['elapsed_time']}")
        print("-------------------------------------------")


tester(function1)
