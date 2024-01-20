from instructions import instructions

def parse(filename):
    with open(filename) as f:
        codelist = [list(i.split()) for i in f.read().split('\n') if len(i.replace(' ', ''))]
    for instruction in codelist:
        insts = [i for i, j in instructions[len(instruction) - 1]]
        try:
            instruction[0] = insts.index(instruction[0].upper())
        except ValueError:
            raise InvalidCommandError()
        for i in range(len(instruction)):
            try:
                instruction[i] = int(instruction[i])
            except ValueError:
                raise InvalidCommandFormatError()
    return codelist

class InvalidCommandError(Exception):
    pass

class InvalidCommandFormatError(Exception):
    pass

