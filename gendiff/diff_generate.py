from gendiff.deserialization import deserialize
from gendiff.find_diff import find_diff
from gendiff.formatters.stylish import get_stylish


def generate_diff(file1, file2, formatter='stylish'):
    file1 = deserialize(file1)
    file2 = deserialize(file2)

    diff = find_diff(file1, file2)
    format_diff = to_format(diff, formatter)

    return format_diff


def to_format(data, formatter):
    if formatter == 'stylish':
        format_data = get_stylish(data)
    return format_data


# print(generate_diff('/home/aleksei/python-project-50/tests/fixtures/input/nested1.json',
# '/home/aleksei/python-project-50/tests/fixtures/input/nested2.json'))