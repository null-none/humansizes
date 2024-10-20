import re


class Humansizes(object):

    def __init__(self):
        self.units = {"B": 1, "KB": 2**10, "MB": 2**20, "GB": 2**30, "TB": 2**40}

    def parse_size(self, size):
        size = size.upper()
        if not re.match(r" ", size):
            size = re.sub(r"([KMGT]?B)", r" \1", size)
        number, unit = [string.strip() for string in size.split()]
        return int(float(number) * self.units[unit])
