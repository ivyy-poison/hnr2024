def parse(filename):
    with open(filename) as f:
        return [[int(j) for j in i.split()] for i in f.read().split('\n')]

def print_value(data, index):
    print(int(data.get(index)))

def set_value(data, index, value):
    data.write(index, value)

def not_value(data, set_index, setter_index):
    data.write(set_index, 0 if data.read(setter_index) else 1)

def add_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, data.read(setter0_index) + data.read(setter1_index))

def subtract_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, data.read(setter0_index) - data.read(setter1_index))

def multiply_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, data.read(setter0_index) * data.read(setter1_index))

def divide_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, data.read(setter0_index) // data.read(setter1_index))

def modulo_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, data.read(setter0_index) % data.read(setter1_index))

def and_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, 1 if data.read(setter0_index) and data.read(setter1_index) else 0)

def or_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, 1 if data.read(setter0_index) or data.read(setter1_index) else 0)

instructions = {
                    1: [
                            print_value
                        ],
                    2: [
                            set_value, not_value
                        ],
                    3: [
                            add_indices, subtract_indices, multiply_indices, divide_indices, modulo_indices, and_indices, or_indices
                        ]
                }
