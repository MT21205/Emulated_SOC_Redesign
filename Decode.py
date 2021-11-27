from defines import *
from Custom_Exceptions import Invalid_Instruction

## Class for the Decode Unit
class Decode:

    # Data members of the Decode class
    __Instruction = 0

    ## Constructor of the Decode Class
    def __init__(self):
        pass

    ## Assigns the Instruction to its  Class member
    def Set_Instruction(self, Inst_In):
        self.__Instruction = Inst_In

    ## Decodes the incoming instruction and stores the content into its data members. 
    #  This data is used by other peripheries to process the instruction further. 
    #  @return Operation_Validity   : Validity flag of the Instruction
    #  @return RS1_Addr             : Address of source register 1
    #  @return RS2_Addr             : Address of source register 2
    #  @return RD_Addr              : Address of destination register
    #  @return Inst_Type            : Type of Instruction under execution
    #  @return Operation_Type       : Type of operation to be  executed
    #  @return Immediate_Data       : Immediate data that can be added to RD or to compute the target address 

    def Decode_Instruction(self):
    
        Operation_Validity = True

        """
        #Source and destination address locations
        RS1_Addr = Inst_In[19:15]
        RS2_Addr = Inst_In[24:20]
        RD_Addr_out = Inst_In[11:7]                
        """

        try:
            # Decoding the Instruction Type
            Inst_Type = self.__Instruction[-6-1:-2] # Type of the instruction executed

            # Raise an exception if an invalid Instruction is detected. 
            if((Inst_Type != IMMEDIATE_TYPE) and (Inst_Type != REGISTER_REGISTER_TYPE) and (Inst_Type != LOAD_TYPE) 
            and (Inst_Type != STORE_TYPE) and (Inst_Type != BRANCH_TYPE) and (Inst_Type != PORT_IN_TYPE) and (Inst_Type != PORT_OUT_TYPE)):
                raise Invalid_Instruction

        except Invalid_Instruction:
            # Handle the exception upon detecting an invalid Instruction
            print("Invalid Instruction Detected. Instruction execution dropped.")
            Operation_Validity = False
            # To avoid the runtime error
            Inst_Type = "00000"
            Operation_Type = "00000"
            Inst_Type = "00000"
            RS1_Addr = "00000"
            RS2_Addr = "00000"
            RD_Addr = "00000"
            Immediate_Data = "00000"

            
        else:
            # Decoding the Operation Type
            Operation_Type = self.__Instruction[-31-1:-25]+ self.__Instruction[-14-1:-12]

            # RS1 address extraction.
            # RS1 doesn't exist for : Port_IN Type Instructions
            RS1_Addr = self.__Instruction[-19-1:-(15)]

            # RS2 address extraction.
            # RS2 doesn't exist for : Immediate, Load and Port Type Instructions
            if((Inst_Type == IMMEDIATE_TYPE) or (Inst_Type == LOAD_TYPE) or (Inst_Type == PORT_IN_TYPE) or (Inst_Type == PORT_OUT_TYPE)):
                RS2_Addr = "00000"
            else:
                RS2_Addr = self.__Instruction[-24-1:-20]

            # RD address extraction.
            # RD doesn't exist for : Branch and Store Type Instructions
            if((Inst_Type == BRANCH_TYPE) or (Inst_Type == STORE_TYPE)):
                RD_Addr = "00000"
            else:
                RD_Addr = self.__Instruction[-11-1:-7]
            
            # Immediate/Offest data extraction.
            # Immediate data exist for : Immediate and Port_IN Type Instruction
            # Offset data exist for : Branch, Load and Store Type Instructions
            if((Inst_Type == IMMEDIATE_TYPE) or (Inst_Type == LOAD_TYPE) or (Inst_Type == PORT_IN_TYPE) ):
                Immediate_Data = self.__Instruction[-31-1:-20]
            elif(Inst_Type == BRANCH_TYPE):
                Immediate_Data = self.__Instruction[-32]+self.__Instruction[-8]+self.__Instruction[-30-1:-25]+self.__Instruction[-11-1:-8]
            elif (Inst_Type == STORE_TYPE):
                Immediate_Data = self.__Instruction[-31-1:-25]+self.__Instruction[-11-1:-7]
            else:
                Immediate_Data = "000000000000"


        return Operation_Validity, Inst_Type, Operation_Type, RS1_Addr, RS2_Addr, RD_Addr, Immediate_Data