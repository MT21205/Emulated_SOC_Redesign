from defines import*

Reg_Data = []
with open (REG_FILE_NAME,"r") as Reg_File:
    for val in Reg_File:
        Reg_Data.append(int(val,BINARY_FORMAT))

## Class for the Register Objects
class Register:

    # Data members of the Register class
    __Address = 0
    __Data = 0

    ## Constructor of the Register class
    def __init__(self,Addr=0):
        if(Addr != 0):
            self.__Address = Addr
            self.__Data = Reg_Data[self.__Address]
        else:
            # Register R0 is hardwired to 0 as per the ISA.
            self.__Address = 0
            self.__Data = 0

    
    ## This method returns the data of the register object calling this method.
    #  @return Data         : Data from the register object calling this method.
    def Get_Register_Data(self):
        return self.__Data

    
    ## This method sets the data of the register object calling this method.
    #  As per the ISA, the register R0 is always hardwired to 0. Hence, its data can't be set explicitly.
    #  @param val_In        : Value that has to be set into the register calling this method.
    def Set_Register_Data(self,val_In):
        if(self.__Address != 0):
            self.__Data = val_In
        else:
            self.__Data = 0


# Creating the objects to each architecture register
Reg = []
for reg_idx in range(REG_CNT):
    Reg_Obj = Register(reg_idx)
    Reg.append(Reg_Obj)