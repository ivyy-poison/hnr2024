from instructions import instructions

def parse(filename):
    with open(filename) as f:
        codelist = [list(i.split()) for i in f.read().split('\n') if len(i.replace(' ', ''))]
    for instruction in codelist:
        insts = [i for i, j in instructions[len(instruction) - 1]]
        instruction[0] = insts.index(instruction[0].upper())
        for i in range(len(instruction)):
            instruction[i] = int(instruction[i])
    return codelist
