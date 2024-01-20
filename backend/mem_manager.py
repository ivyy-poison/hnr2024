class MemoryManager:
    mem_dict = dict()

    def read(self, loc: int):
        try:
            return self.mem_dict[loc]
        except KeyError:
            raise LocNoDataError(loc)

    def write(self, loc: int, val):
        self.mem_dict[loc] = val

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