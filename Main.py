from ALU import *
from Decode import *
from Memory import *
from Register import *
from Port import In_Port, Out_Port

# Import the required constants from the defines file
from defines import *

# Creation of Objects to the Memory, Decode, ALU and the Register classes

DE = Decode()
EX = ALU()
Inst_Mem = Inst_Memory()
Data_Mem = Data_Memory()
REG = Register()

Instructions_Cnt = Inst_Mem.Get_Memory_Size()
## PC  : Program counter
PC = 0
# Execute for each instruction from the Instruction Memory
while(PC != Instructions_Cnt):

    ## Branch_Flag : Indicates if a Branch has to take place or not.
    Branch_Flag = False

    # Read the instruction from the Instruction Memory
    ## Inst_Validity : Checks the validity of the instruction.
    Inst_Validity, Instruction = Inst_Mem.Get_Data(PC)
    if(Inst_Validity == False):
        # As the Instruction access is termed invalid, the instruction execution is terminated and next instruction is processed
        PC = PC +1
        continue
    else:
        pass

    # If the Instruction is valid, Decode the Instruction.
    Operation_Validity = DE.Decode_Instruction(Instruction)

    if(Operation_Validity == False):
        # As the operation is termed invalid, the instruction execution is terminated and next instruction is processed
        PC = PC +1
        continue
    else:
        pass

    # If the Decoded Instruction is valid, extract the register address, Inst, Operation Types and the Immediate Data.
    ## RS1_Addr     : Address of source register 1
    ## RS2_Addr     : Address of source register 2
    ## RD_Addr      : Address of destination register
    RS1_Addr, RS2_Addr, RD_Addr = DE.Get_Register_Address()

    ## Instruction_Type : Type of Instruction under execution
    ## Operation_Type   : Type of operation to be  executed
    Instruction_Type, Operation_Type = DE.Get_Instruction_Operation_Type()
    

    # Extraction of the registers RS1 and RS2 Data
    ## RS1  : Value of RS1 register
    ## RS2  : Value of RS2 register
    RS1 = Reg[RS1_Addr].Get_Register_Data()
    RS2 = Reg[RS2_Addr].Get_Register_Data()

    # Set the decoded data into the ALU class data members to make it available for execution.
    EX.Set_Source_Registers(RS1, RS2)
    EX.Set_Immediate_Data(DE.Get_Immx_Data())
    EX.Set_Instruction_Operation_Types(Instruction_Type, Operation_Type)

    # Perform the ALU operation. Post the ALU operation, read the ALU Result
    Branch_Flag, Operation_Validity = EX.ALU_Perform_Operation()
    Result = EX.Get_ALU_Result()

    if(Operation_Validity == False):
        # As the operation is termed invalid, the instruction execution is terminated and next instruction is processed
        PC = PC +1
        continue
    else:
        pass

    if(Branch_Flag == True):
        # Branch to the required instruction if the Branch is detected and is true.
        PC = Result
        continue
    else:
        pass

    # Perform the LOAD or Store operation on the Data Memory exclusively for the LOAD or STORE type instructions.
    if(Instruction_Type == LOAD_TYPE):
        Inst_Validity, Result = Data_Mem.Get_Data(Result)
        Result = int(Result, BINARY_FORMAT)
    elif(Instruction_Type == STORE_TYPE):
        Inst_Validity = Data_Mem.Set_Data(Result,RS2)
    else:
        pass
    
    if(Inst_Validity == False):
        # As the Address access is termed invalid, the instruction execution is terminated and next instruction is processed
        PC = PC +1
        continue
    else:
        pass


    # The final value of the registers has to be written iff the Instructions aren't of TYPE STORE, BRANCH or PORT type.
    if((Instruction_Type != STORE_TYPE) and (Instruction_Type != BRANCH_TYPE) and (Instruction_Type != PORT_IN_TYPE) 
    and (Instruction_Type != PORT_OUT_TYPE)):
        Reg[RD_Addr].Set_Register_Data(Result)
    else:
        pass

    # Read the Port input data and process it for the PORT_IN_TYPE instruction. 
    if(Instruction_Type == PORT_IN_TYPE):
        # Move the Immediate data contents from the Execute stage to the Port.
        In_Port[RD_Addr].Set_Input_Port(Result)

    # Output the required data onto the Output port for PORT_OUT_TYPE instructions.
    elif(Instruction_Type == PORT_OUT_TYPE):
        Out_Port[RD_Addr].Set_Output_Port(Result)
    else:
        pass
    
    # After processing the current instruction, increement PC to point to next instruction.
    PC = PC +1