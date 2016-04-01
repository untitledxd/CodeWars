# def reverse_it(data):
#     if isinstance(data, bool) or not isinstance(data, (int, float, str)):
#         return data
#     elif isinstance(data, str):
#         return data[::-1]
#     elif isinstance(data, int):
#         return int(str(data)[::-1])
#     else:  # float
#         return float(str(data)[::-1])


def reverse_it(data):
    if type(data) in (int, str, float):
        return type(data)(str(data)[::-1])
    return data