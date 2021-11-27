from defines import INPUT_PORT_CNT
from defines import OUTPUT_PORT_CNT
from Register import Reg
from abc import abstractmethod

## Class for the Port Units
class Port:
    __Addr = 0
    __Data = 0
    def __init__(self):
        Output_Port_File_Name = "Port_Data.txt"

        # Clearing the Port data before the start of the execution
        fp = open(Output_Port_File_Name,'w')
        fp.close()

    @abstractmethod
    def Set_Port_Data(self):
        pass
    

## Class for the Input Ports
class Input_Port(Port):
    def __init__(self, Addr):
        super().__init__()
        self.__Addr = Addr


    def Set_Port_Data(self, Data):
        self.__Data = Data
        # Register 31 is the destination register that stores the content input from any port input
        Reg[31] = self.__Data

## Class for the Output Ports
class Output_Port(Port):
    Output_Port_File_Name = "Port_Data.txt"
    def __init__(self, Addr):
        super().__init__()
        self.__Addr = Addr

    def Set_Port_Data(self):
        self.__Data = Reg[31]

        self.OP_Display_Data()
        self.OP_Write_to_File()

    ## Display method for the PORT output operation
    def OP_Display_Data(self):
        print("Output Port OP{} : {}".format(self.__Addr, self.__Data))
    
    ## Function to write the data transmitted to the output PORT onto a file. 
    def OP_Write_to_File(self):
        with open(self.Output_Port_File_Name,'a') as file_obj:
            file_obj.write("OP{} : {}".format(self.__Addr, self.__Data))
            file_obj.close()
 


In_Port = []
Out_Port = []
for idx in range(INPUT_PORT_CNT):
    IP = Input_Port(idx)
    In_Port.append(IP)

for idx in range(OUTPUT_PORT_CNT):
    OP = Output_Port(idx)
    Out_Port.append(OP)
