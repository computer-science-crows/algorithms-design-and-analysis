import json
import os
import time
from colored import fore, back, style
from app.tools import save_data


def tester(function):
    cwd = os.getcwd()
    cwd += "/corruption-strategy/json"

    # gets test cases from json
    test_cases = {}
    with open(cwd+"/test_cases.json", "r") as read_it:
        test_cases = json.load(read_it)

    # deletes previous tests for this function
    with open(cwd+f"/tests/{function.__name__}.json", "w") as write_it:
        json.dump([], write_it)

    # prints function test in console
    print(style.BOLD + f"Testing {function.__name__}" + style.RESET)
    print("-------------------------------------------")

    # for each test case calls the function with the specified parameters, times it and checks if the solution matches the
    # optimal one obtained previously using backtrack. These results are saved in a json file
    failed_tc = 0
    for index, tc in enumerate(test_cases):
        try:
            testing_data = {}

            start = time.time()
<<<<<<< Updated upstream
            testing_data["f_result"], testing_data["f_value"] = function(
=======
            testing_data["cities"], testing_data["roads"], testing_data["profit"] = function(
>>>>>>> Stashed changes
                tc['n'], tc['m'], tc['a'], tc['w'])
            end = time.time()

            testing_data["elapsed_time"] = end - start

            testing_data["matches"] = False
            if testing_data["profit"] == tc["optimal_value"]:
                testing_data["matches"] = True

            save_data(testing_data, f"/tests/{function.__name__}.json")

            # prints test results
            print(f"Test case #{index + 1} -> " + back.RED + style.BOLD +
                  "FAILED" + style.RESET if testing_data['matches'] == False else f"Test case #{index + 1} -> " + back.GREEN + style.BOLD +
                  "SUCCESS" + style.RESET)
<<<<<<< Updated upstream
            print(f"  result: {testing_data['f_result']}")
            print(f"  value: {testing_data['f_value']}")
=======
            print(f"  cities: {testing_data['cities']}")
            print(f"  roads: {testing_data['roads']}")
            print(f"  profit: {testing_data['profit']}")

            # If FAILED
>>>>>>> Stashed changes
            if not testing_data['matches']:
                print(f"   optimal value: {tc['optimal_value']}")
            print(f"  elapsed time: {testing_data['elapsed_time']}")
            print("-------------------------------------------")

        # If exception in function occured
        except Exception as ex:
            failed_tc += 1
            print(f"Test case #{index + 1} -> " + back.RED + style.BOLD +
                  "FAILED" + style.RESET)
            print("An Exception ocurred!!")
            print("-------------------------------------------")
            print(ex)

    return (f'Failed: {failed_tc}')
