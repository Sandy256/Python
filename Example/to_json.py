# import json
# from functools import wraps
#
#
# def to_json(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return json.dumps(func(*args, **kwargs))
#
#     return wrapper
#
#
# @to_json
# def get_data():
#     return {'data': 42}
#
#
# s = get_data()  # вернёт '{"data": 42}'
# print(s)

import functools
import json


def to_json(func):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped