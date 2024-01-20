class MemoryManager:
    def __init__(self, user_input_str : str):
        self.pc_register = 0
        self.mem_dict = dict()
        self.user_inputs = [ln for ln in user_input_str.split('\n') if len(ln.replace(" ", ""))]
        self.user_input_count = 0
        self.print_vals = []

    def read(self, loc: int):
        try:
            return self.mem_dict[loc]
        except KeyError:
            raise LocNoDataError(loc)

    def write(self, loc: int, val) -> None:
        self.mem_dict[loc] = val

    def set_pc_register(self, pc : int) -> None:
        if pc < 0:
            raise InvalidLineError()
        self.pc_register = pc
    
    def increment_pc_register(self) -> None:
        self.pc_register += 1
    
    def read_pc_register(self) -> int:
        return self.pc_register
    
    def print_to_screen(self, val) -> None:
        self.print_vals.append(val)

    def get_outputs(self):
        return self.print_vals
    
    def get_user_input(self):
        if self.user_input_count >= len(self.user_inputs):
            raise NoUserInputError()
        output_val = self.user_inputs[self.user_input_count]
        self.user_input_count += 1
        return output_val

class LocNoDataError(IndexError):
    pass

class InvalidLineError(Exception):
    pass

class NoUserInputError(Exception):
    pass

def test_mem_manager():
    test_mem = MemoryManager()
    try:
        test_mem.read(1)
    except LocNoDataError:
        pass

    test_mem.write(1, 5)
    assert test_mem.read(1) == 5
    print("All tests passed for memory manager")
