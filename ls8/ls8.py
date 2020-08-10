#!/usr/bin/env python3

"""Main."""

# import sys
# from cpu import *


 
# cpu = CPU()

# cpu.load()
# cpu.run()

import sys
print(sys.argv)
from cpu import *

def main(argv):
    """Main."""
    if len(argv) != 2:
        print(f"usage: {argv[0]} filename", file=sys.stderr)
        return 1
    cpu = CPU()
    cpu.load(argv[1])
    # cpu.load()
    cpu.run()
    return 0
if __name__ == "__main__":
    sys.exit(main(sys.argv))





    # Tim's 

    # try:
#     file = open('examples/print8.ls8', 'r')
#     lines = file.read()
#     raise Exception("hi")
#     file.close()
# except Exception:
#     print(file.closed)




# import sys
# ​
# # if you forget the filename
# if len(sys.argv) < 2:
#     print("did you forget the file to open?")
#     print('Usage: filename file_to_open')
#     sys.exit()
# ​
# self.ram = [None] * 256
# address = 0
# ​
# try:
#     with open(sys.argv[1]) as file:
#         for line in file:
#             comment_split = line.split('#')
# ​
#             possible_num = comment_split[0]

#             if possible_num == '':
#                 continue
# ​
#             if possible_num[0] == '1' or possible_num[0] == '0':
#                 num = possible_num[:8]
# ​
#                 print(f'{num}: {int(num, 2)}')
# ​
#                 self.ram[address] = int(num, 2)
#                 address += 1
# ​
# ​
# ​
# except FileNotFoundError:
#     print(f'{sys.argv[0]}: {sys.argv[1]} not found')