import json


def load_config():
    """

    :return:
    """

    with open('config.json', 'r') as file:
        data = json.load(file)
    return data
