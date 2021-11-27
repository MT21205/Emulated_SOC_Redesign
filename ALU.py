from defines import *                           # Importing the constants
from Custom_Exceptions import Divide_By_Zero    # Importing the custom exception


## Class for the ALU Unit
class ALU:

    # These are the data members of the ALU class that stores these data prior to performaning any operation.
    __RS1 = 0
    __RS2 = 0
    __Inst_Type = 0
    __Operation_Type = 0
    __Immediate_Data = 0
    __ALU_Result = 0

    ## Constructor of the ALU class
    def __init__(self,RS1 = 0, RS2 = 0, Instruction_Type = 0, Operation_Type = 0, Immediate_Data = 0, Result = 0):
        self.__RS1 = RS1
        self.__RS2 = RS2
        self.__Inst_Type = Instruction_Type
        self.__Operation_Type = Operation_Type
        self.__Immediate_Data = Immediate_Data
        self.__ALU_Result = Result

    ## Function to set the source registers at the Execute/ALU Stage
    #  @param RS1   : Source Register 1
    #  @param RS2   : Source Register 2
    def Set_Source_Registers(self, RS1, RS2):
        self.__RS1 = RS1
        self.__RS2 = RS2
    
    ## Function to set the Immediate or Offset at the Execute/ALU Stage
    #  @param Imm_Data  : Immediate Data Value
    def Set_Immediate_Data(self, Imm_Data):
        self.__Immediate_Data = Imm_Data
    
    ## Function to set the Operation and Instruction Types at the Execute/ALU Stage
    #  @param Instruction_Type  : Type of the Instruction under process
    #  @param Op_Type           : Type of the Operation to be performed
    def Set_Instruction_Operation_Types(self, Instruction_Type, Op_Type):
        self.__Inst_Type = Instruction_Type
        self.__Operation_Type = Op_Type

    ## This method returns the result from the ALU class
    #  @return ALU_Result   : Result from the ALU operation
    def Get_ALU_Result(self):
        return self.__ALU_Result


    ## This method performs the ALU operation with the data available in it's data members.
    #  @return Branch_flag          : Indicates if a branch has to be staken or not
    #  @return Operation_Validity   : Indicates if the Instruction currently being executed as valid or not.
    def ALU_Perform_Operation(self):
        self.__ALU_Result = 0
        Branch_flag = False
        Operation_Validity = True

        # The ALU operations are performed based on the Instruction Type
        if(self.__Inst_Type == IMMEDIATE_TYPE):
            self.__ALU_Result = self.__RS1 + self.__Immediate_Data
        elif(self.__Inst_Type == REGISTER_REGISTER_TYPE):
            
            # For the Reg-Reg Type INstructions, the operations are performed based on the Operation Type 
            if(self.__Operation_Type == AND):
                self.__ALU_Result = self.__RS1 & self.__RS2
            elif(self.__Operation_Type == OR):
                self.__ALU_Result = self.__RS1 | self.__RS2
            elif(self.__Operation_Type == ADD):
                self.__ALU_Result = self.__RS1 + self.__RS2
            elif(self.__Operation_Type == SUB):
                self.__ALU_Result = self.__RS1 - self.__RS2
            elif(self.__Operation_Type == SL):
                self.__ALU_Result = self.__RS1 << self.__RS2
            elif(self.__Operation_Type == SR):
                self.__ALU_Result = self.__RS1 >> self.__RS2
            elif(self.__Operation_Type == MUL):
                self.__ALU_Result = self.__RS1 * self.__RS2
            elif(self.__Operation_Type == DIV):
                # Prior to perform the division, the divisor is check to avoid a divide by 0.
                # If the divisor is 0, an exception is raised.
                try:
                    if(self.__RS2 == 0):
                        raise Divide_By_Zero
                except Divide_By_Zero:
                    print("Attempt to divide by 0. Operation invalidated and skipped.")
                    Operation_Validity = False
                else:
                    self.__ALU_Result = self.__RS1 / self.__RS2
            else:
                self.__ALU_Result = 0

        # For a Load or a Store operation, the result of the ALU will be the memory address.
        elif((self.__Inst_Type == LOAD_TYPE) or (self.__Inst_Type == STORE_TYPE)):
            self.__ALU_Result = self.__RS1 + self.__Immediate_Data

        # For a Branch instruction, the ALU result is the branch address.
        elif(self.__Inst_Type == BRANCH_TYPE):
            self.__ALU_Result = self.__Immediate_Data
            Branch_flag = True

        elif(self.__Inst_Type == PORT_IN_TYPE):
            self.__ALU_Result = self.__Immediate_Data
        elif(self.__Inst_Type == PORT_OUT_TYPE):
            self.__ALU_Result = self.__RS1

        else:
            self.__ALU_Result = 0

        return Branch_flag, Operation_Validity