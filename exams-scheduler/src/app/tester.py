import json
import os
import time
from colored import fore, back, style
from app.tools import save_data


def tester(function, solver):
    cwd = os.getcwd()
    cwd += "/json"

    # gets test cases from json
    test_cases = {}
    with open(cwd+"/test_cases.json", "r") as read_it:
        test_cases = json.load(read_it)

    # deletes previous tests for this function
    with open(cwd+f"/tests/{solver.__name__}.json", "w") as write_it:
        json.dump([], write_it)

    # prints function test in console
    print(style.BOLD + f"Testing {solver.__name__}" + style.RESET)
    print("-------------------------------------------")

    # for each test case calls the function with the specified parameters, times it and checks if the solution matches the
    # optimal one obtained previously using backtrack. These results are saved in a json file
    failed_tc_count = 0
    failed_tc = []
    for index, tc in enumerate(test_cases):
        try:
            testing_data = {}

            start = time.time()
            testing_data["solution"], testing_data["value"] = function(
                tc['k'], tc['propositions'], solver)
            end = time.time()

            testing_data["elapsed_time"] = end - start

            testing_data["matches"] = False
            if testing_data["value"] == tc["optimal_value"]:
                testing_data["matches"] = True

            save_data(testing_data, f"/tests/{solver.__name__}.json")

            # prints test results
            print(f"Test case #{index + 1} -> " + back.RED + style.BOLD +
                  "FAILED" + style.RESET if testing_data['matches'] == False else f"Test case #{index + 1} -> " + back.GREEN + style.BOLD +
                  "SUCCESS" + style.RESET)
            print(f"  solution: {testing_data['solution']}")
            print(f"  value: {testing_data['value']}")

            # If FAILED
            if not testing_data['matches']:
                print(f"   solution: {tc['optimal_solution']}")
                print(f"   optimal value: {tc['optimal_value']}")
            print(f"  elapsed time: {testing_data['elapsed_time']}")
            print("-------------------------------------------")

        # If exception in function occured
        except Exception as ex:
            failed_tc_count += 1
            print(f"Test case #{index + 1} -> " + back.RED + style.BOLD +
                  "FAILED" + style.RESET)
            print("An Exception ocurred!!")
            print("-------------------------------------------")
            print(ex)
            failed_tc.append((index + 1, ex))

    print(f'{failed_tc_count} exception(s) occured while testing.')
    for ftc in failed_tc:
        print(ftc)

    return (f'Failed: {failed_tc_count}')
