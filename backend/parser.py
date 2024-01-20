def parse(filename):
    with open(filename) as f:
        return [[int(j) for j in i.split()] for i in f.read().split('\n') if len(i.replace(' ', ''))]
