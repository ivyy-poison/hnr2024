import os

if __name__ == "__main__":
    args = os.sys.argv
    temp = args[2]
    temp_arr = temp.split("\n")

    
    print(f'hello world with args: {"".join(temp_arr)}')
    # raise Exception("hello world")
