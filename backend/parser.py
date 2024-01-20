def parse(filename):
    with open(filename) as f:
        return [[int(j) for j in i.split()] for i in f.read().split('\n')]

def print_value(data, index):
    print(int(data.get(index)))

def set_value(data, index, value):
    data.set(index, value)

def not_value(data, set_index, setter_index):
    data.set(set_index, 0 if data.get(setter_index) else 1)

def add_indices(data, set_index, setter0_index, setter1_index):
    data.set(set_index, data.get(setter0_index) + data.get(setter1_index))

instructions = {
                    1: [
                            print_value
                        ],
                    2: [
                            set_value, not_value
                        ],
                    3: [
                            add_indices
                        ]
                }
