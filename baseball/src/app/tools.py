import json
import os


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


def Memoize(f):
    dict = {}

    def memoized_function(*args):
        if args in dict:
            return dict[args]
        else:
            result = f(*args)
            dict[args] = result
            return result
    return memoized_function
