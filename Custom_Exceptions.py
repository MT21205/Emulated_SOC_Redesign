## Exception raised for a divide by 0 attempt
class Divide_By_Zero(Exception):
    def __init__(self):
        pass

## Exception raised for an Invalid Instruction 
class Invalid_Instruction(Exception):
    def __init__(self):
        pass

## Exception raised for an access to out of bounds Memory
class Memory_Out_Of_Bound(Exception):
    def __init__(self):
        pass