from defines import *
from Custom_Exceptions import Invalid_Instruction

## Class for the Decode Unit
class Decode:

    # Data members of the Decode class
    __RS1_Addr = 0
    __RS2_Addr = 0
    __RD_Addr = 0
    __Inst_Type = 0
    __Immediate_Data = 0
    __Operation_Type = 0

    ## Constructor of the Decode Class
    def __init__(self):
        pass

    ## Returns the source and destination registers address. 
    #  @return RS1_Addr : Source register 1 address
    #  @return RS2_Addr : Source register 2 address
    #  @return RD_Addr  : Destination register address
    def Get_Register_Address(self):
        return int(self.__RS1_Addr, BINARY_FORMAT), int(self.__RS2_Addr, BINARY_FORMAT), int(self.__RD_Addr, BINARY_FORMAT)

    ## Returns the Immediate data from the decoded instruction
    #  @return Immx_Data : The Immediate data from the instruction
    def Get_Immx_Data(self):
        return int(self.__Immediate_Data, BINARY_FORMAT)

    ## Returns the Instruction and Operation type from the decoded Instruction. 
    #  @return Inst_Type        : Type of the Instruction to be processed. 
    #  @return Operation_Type   : Type of the operation to be performed.
    def Get_Instruction_Operation_Type(self):
        return self.__Inst_Type, self.__Operation_Type 

    
    ## Decodes the incoming instruction and stores the content into its data members. 
    #  This data is used by other peripheries to process the instruction further. 
    #  @param Inst_In               : Instruction to be decoded
    #  @return Operation_Validity   : Validity flag of the Instruction
    def Decode_Instruction(self,Inst_In):
    
        Operation_Validity = True

        """
        #Source and destination address locations
        RS1_Addr = Inst_In[19:15]
        RS2_Addr = Inst_In[24:20]
        RD_Addr_out = Inst_In[11:7]                
        """

        try:
            # Decoding the Instruction Type
            Inst_Type = Inst_In[-6-1:-2] # Type of the instruction executed

            # Raise an exception if an invalid Instruction is detected. 
            if((Inst_Type != IMMEDIATE_TYPE) and (Inst_Type != REGISTER_REGISTER_TYPE) and (Inst_Type != LOAD_TYPE) 
            and (Inst_Type != STORE_TYPE) and (Inst_Type != BRANCH_TYPE) and (Inst_Type != PORT_IN_TYPE) and (Inst_Type != PORT_OUT_TYPE)):
                raise Invalid_Instruction

        except Invalid_Instruction:
            # Handle the exception upon detecting an invalid Instruction
            print("Invalid Instruction Detected. Instruction execution dropped.")
            Operation_Validity = False
            
        else:
            self.__Inst_Type = Inst_Type

            # Decoding the Operation Type
            self.__Operation_Type = Inst_In[-31-1:-25]+Inst_In[-14-1:-12]

            # RS1 address extraction.
            # RS1 doesn't exist for : Port_IN Type Instructions
            self.__RS1_Addr = Inst_In[-19-1:-(15)]

            # RS2 address extraction.
            # RS2 doesn't exist for : Immediate, Load and Port Type Instructions
            if((Inst_Type == IMMEDIATE_TYPE) or (Inst_Type == LOAD_TYPE) or (Inst_Type == PORT_IN_TYPE) or (Inst_Type == PORT_OUT_TYPE)):
                self.__RS2_Addr = "00000"
            else:
                self.__RS2_Addr = Inst_In[-24-1:-20]

            # RD address extraction.
            # RD doesn't exist for : Branch and Store Type Instructions
            if((Inst_Type == BRANCH_TYPE) or (Inst_Type == STORE_TYPE)):
                self.__RD_Addr = "00000"
            else:
                self.__RD_Addr = Inst_In[-11-1:-7]
            
            # Immediate/Offest data extraction.
            # Immediate data exist for : Immediate and Port_IN Type Instruction
            # Offset data exist for : Branch, Load and Store Type Instructions
            if((Inst_Type == IMMEDIATE_TYPE) or (Inst_Type == LOAD_TYPE) or (Inst_Type == PORT_IN_TYPE) ):
                self.__Immediate_Data = Inst_In[-31-1:-20]
            elif(Inst_Type == BRANCH_TYPE):
                self.__Immediate_Data = Inst_In[-32]+Inst_In[-8]+Inst_In[-30-1:-25]+Inst_In[-11-1:-8]
            elif (Inst_Type == STORE_TYPE):
                self.__Immediate_Data = Inst_In[-31-1:-25]+Inst_In[-11-1:-7]
            else:
                self.__Immediate_Data = "000000000000"


        return Operation_Validity