

def NAND_gate(a, b):  # Return 1 if a or b is 0
    if a:
        if b:
            return 0
    return 1


def NOT_gate(a):  # Returns opposite of input i.e 1 returns 0
    return NAND_gate(a, a)


def AND_gate(a, b):  # will return 1 if both a and b is 1, else 0
    return NOT_gate(NAND_gate(a, b))


def OR_gate(a, b):  # Any one of a, b or both can be on to return 1, else 0
    return NAND_gate(NAND_gate(a, a), NAND_gate(b, b))


def XOR_gate(a, b):  # will return 1 if a or b is on 1, else 0
    return AND_gate(NAND_gate(a, b), OR_gate(a, b))


def half_adder(a, b):
    s = XOR_gate(a, b)  # will return 1 if a or b is on 1, else 0
    c = AND_gate(a, b)  # will return 1 if both a and b is 1
    return s, c


def full_adder(a, b, c):
    gate_a = XOR_gate(a, b)
    s = XOR_gate(XOR_gate(a, b), c)
    carry_1 = AND_gate(gate_a, c)  # check for carry out with either a or b and c, will return 1 if both arguments are 1
    carry_2 = AND_gate(a, b)  # check for carry out with a or c, will return 1 if both arguments are 1
    c_out = OR_gate(carry_1, carry_2)  # # will return 1 if either arguments are 1
    return s, c_out


# ALU that takes in inputs and either produces output from a half adder or from a full adder
# if the opcode is 0, we will return the output from the half_adder(), else full_adder()
def ALU(a, b, c, opcode):
    if opcode == 0:
        s, c = half_adder(a, b)
    else:
        s, c = full_adder(a, b, c)
    return s, c
