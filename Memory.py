from defines import *
from Custom_Exceptions import Memory_Out_Of_Bound

## Class for the Memory objects
class Memory:

    # Data members of the Memory class
    __Data = []
    __Mem_Size = 0

    ## Constructor of the Memory class
    def __init__(self, File_Name):

        # Read the contents from the memory file and initialize the Memory.
        self.__Data = []
        with open(File_Name,"r") as Mem_Obj:
            for Data in Mem_Obj:
                self.__Data.append(Data.strip("\n"))
            # Read the len of the Memory.
            self.__Mem_Size = len(self.__Data)

    ## Returns the size of the Memory
    #  @return Mem_Size         : Size of the calling memory object (i.e., Data or the Instruction memory)
    def Get_Memory_Size(self):
        return self.__Mem_Size

    ## This method returns the contents of the Memory as per the input address
    #  @param Addr              : Address from which the data has to be fetched
    #  @return Inst_Validity    : Validity of the Instruction accessing the data
    #  @return Data             : Data from the memory of the specified address
    def Get_Data(self, Addr):
        Inst_Validity  = False

        # Prior to fetching the data from the memory, check if the requested address is within the memory range.
        try:
            if(Addr >= self.__Mem_Size):
                raise(Memory_Out_Of_Bound)
        except Memory_Out_Of_Bound:
            # Access to memory is performed beyond the bounds
            print("Access to Memory out of Range")
            return Inst_Validity, 0
        else:
            Inst_Validity = True
            return Inst_Validity, self.__Data[Addr]


    ## This method sets the data into the memory of the address specified.
    #  @param Addr              : Address at which the data has to be set.
    #  @param Value             : Data that has to be written to the memory specified by the Addr.
    #  @return Inst_Validity    : Indicates the validity of the instruction if it is pointing to a valid address or not.
    def Set_Data(self, Addr, Value):
        Inst_Validity  = False
        try:
            if(Addr >= self.__Mem_Size):
                raise(Memory_Out_Of_Bound)
        except Memory_Out_Of_Bound:
            print("Access to Memory out of Range")
        else:
            Inst_Validity = True
            self.__Data[Addr] = Value
        return Inst_Validity


# Data memory and the Instruction memory share the same attributes as the memory.
# Hence, they tend to inherit from the base class Memory. 

## Data memory class. A child class of the Memory class.
class Data_Memory(Memory):
    def __init__(self):
        super().__init__(DATA_MEM_FILE)

## Instruction memory class. A child class of the Memory class.
class Inst_Memory(Memory):
    def __init__(self):
        super().__init__(INST_MEM_FILE)