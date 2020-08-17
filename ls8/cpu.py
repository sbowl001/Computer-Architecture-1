"""CPU functionality."""

import sys
print(sys.argv)

LDI = 0b10000010  # LDI R0,8 130
PRN = 0b01000111  # PRN R0, 71
HLT = 0b00000001  # HLT
MUL = 0b10100010  # Multiply
POP = 0b01000110
PUSH = 0b01000101
CALL = 0b01010000
RET = 0b00010001
ADD = 0b10100000

SP = 7 

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""

        self.ram = [0] * 256 
        self.reg = [0] * 8
        self.pc = 0
         
        pass

    def load(self, filename = None):
        """Load a program into memory."""

        try: 
            address = 0
            # filename = sys.argv[1]

            with open(filename) as fp: 
                for line in fp:
                    comment_split = line.split("#")
                # line . split 
                # by some sign 
                    num = comment_split[0].strip()
                # strip those 
                    if num == '':
                        continue  
                # if strip value = () , continue 
                    val = int(num, 2)
                    self.ram[address] = val 
                    address += 1 
                # self.ram[address] =  value that you get 
                # address += 1 
        except FileExistsError:
            print('Error file not found')
            sys.exit(2)

        # For now, we've just hardcoded a program:
#  don't need this anymore? 
#         program = [
#             # From print8.ls8
#             0b10000010, # LDI R0,8
#             0b00000000,
#             0b00001000,
#             0b01000111, # PRN R0
#             0b00000000,
#             0b00000001, # HLT
#         ]

#         for instruction in program:
#             self.ram[address] = instruction
#             address += 1
    def ram_read(self, mar):
        return self.ram[mar]
    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr 
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print("hello")
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        self.load(sys.argv[1])
        # self.load()
        # running = True 

        while True: 
            pc = self.pc 
            ir = self.ram_read(pc)
        # LDI
            if ir == LDI: 
                self.reg[self.ram_read(pc + 1)] = self.ram_read(pc + 2)
                self.pc += 3
        # HLT
            elif ir == HLT: 
                # running = False
                sys.exit(1)
        # PRN
            elif ir == PRN: 
                print(self.reg[self.ram_read(pc + 1)])
                self.pc += 2
            elif ir == MUL: 
                a = self.ram_read(pc + 1)
                b = self.ram_read(pc + 2)
                self.alu('MUL', a, b)
                self.pc += 3 
        # Push  
            elif ir == PUSH:
                self.trace()
                self.reg[SP] = 0xF4
                self.reg[SP] -= 1 
                stack_address = self.reg[SP]
                register_num = self.ram_read(pc + 1)
                # self.trace()
                value = self.reg[register_num]
                self.ram_write(stack_address, value)
                self.pc += 2 
                
            elif ir == POP: 
                stack_value = self.ram_read(self.reg[SP])

                register_num = self.ram_read(pc + 1)

                self.reg[register_num] = stack_value

                self.reg[SP] += 1 
                self.pc += 2 
            elif ir == CALL:
                self.reg[SP] -= 1
                stack_address = self.reg[SP]
                returned_address = pc + 2
                self.ram_write(stack_address, returned_address)
                register_num = self.ram_read(pc + 1)
                self.pc = self.reg[register_num]

            elif ir == RET: 
                self.pc = self.ram_read(self.reg[SP])
                self.reg[SP] += 1 
            
            elif ir == ADD:
                a = self.ram_read(pc + 1)
                b = self.ram_read(pc + 2)
                self.alu("ADD", a, b)
                self.pc += 3 
   
