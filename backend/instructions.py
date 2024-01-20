def print_value(data, index):
    print(int(data.get(index)))

def set_value(data, index, value):
    data.write(index, value)

def not_index(data, set_index, setter_index):
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
                            ('PRINT_VALUE', print_value)
                        ],
                    2: [
                            ('SET', set_value), ('NOT', not_index)
                        ],
                    3: [
                            ('ADD', add_indices), ('SUB', subtract_indices),
                            ('MULT', multiply_indices), ('DIV', divide_indices), ('MOD', modulo_indices),
                            ('AND', and_indices), ('OR', or_indices)
                        ]
                }
