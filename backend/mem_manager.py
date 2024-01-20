class MemoryManager:
    pc_register = 0
    mem_dict = dict()

    def __init__(self):
        self.pc_register = 0

    def read(self, loc: int):
        try:
            return self.mem_dict[loc]
        except KeyError:
            raise LocNoDataError(loc)

    def write(self, loc: int, val):
        self.mem_dict[loc] = val

    def set_pc_register(self, pc : int):
        self.pc_register = pc
    
    def increment_pc_register(self):
        self.pc_register += 1
    
    def read_pc_register(self):
        return self.pc_register

class LocNoDataError(Exception):
    def __init__(self, loc : int):
        super().__init__(f"Memory at location {loc} has no data")


def test_mem_manager():
    test_mem = MemoryManager()
    try:
        test_mem.read(1)
    except LocNoDataError:
        pass

    test_mem.write(1, 5)
    assert test_mem.read(1) == 5
    print("All tests passed for memory manager")