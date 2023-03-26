import json
import os
import time
import ast

cwd = os.getcwd()
cwd += "/baseball/json"
print(cwd)

t = {"[1, 2, 3, 4, 5]": "SO"}
with open(cwd+"/test_cases.json", "w") as write_it:
    json.dump(t, write_it)


def function(l):
    print(l)


def tester(function):
    test_cases = {}
    with open(cwd+"/test_cases.json", "r") as read_it:
        test_cases = json.load(read_it)

    for tc in test_cases:
        print(tc)
        start = time.time()
        res = ast.literal_eval(tc)
        print(i for i in res)
        end = time.time()
        print(f"elapsed time: {end - start}")


tester(function)
