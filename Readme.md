# Emulated SOC Design

This project aims at providing the simulated functionality of the SOC when the assembly instructions (i.e., encoded in 1's and 0's) are to be processed.
The choice of the Instruction Set Architecture(ISA) is the RV32I. It is a 32-bit instruction set with each instruction, data and memory of size 32-bits.
Hence, the memory here is word addressable.


# Top level view of the design and the SOC components
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ ++++++    +++++++++++++++++++++++++++++                   +
+ + PC +    +           MEMORY          +                   +
+ ++++++    +                           +                   +
+           + +++++++++++   +++++++++++ +                   +
+           + +   Inst  +   +   Data  + +                   +
+           + +   Mem   +   +   Mem   + +                   +
+           + +++++++++++   +++++++++++ +                   +
+           +                           +                   +
+           +                           +                   +
+           +++++++++++++++++++++++++++++                   +
+                                                           +
+   +++++++++++                               +++++++++++   +
+   +         +                               +         +   +
+   +   In    +                               +   Out   +   +
+   +   Port  +                               +   Port  +   +
+   +         +                               +         +   +
+   +++++++++++                               +++++++++++   +
+                                                           +
+                                                           +
+   +++++++++++         +++++++++++           +++++++++++   +
+   +         +         +         +           +         +   +
+   +   ALU   +         + Decode  +           +   Reg   +   +
+   +         +         +         +           +         +   +
+   +++++++++++         +++++++++++           +++++++++++   +
+                                                           +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```

This top level view of the design shows the objects with the obect oriented design approach.
These provides the inputs for the choice of classes to de designed along with the ones that can inherit the features from the parent class.
Ex: The Memory class with it's child classes as Inst_Mem and DData_Mem.


# Instruction encoding and format

The following are the instructions used and their encoding format as per the chosen 32-bit ISA

**Source : [ISA](https://msyksphinz-self.github.io/riscv-isadoc/html/rvi.html#xor)**

Note: For the port operations, the register R[31] is treated as ACC register.

The rest of the Instructions outside this ISA are as below:
 - Port IN:
```
+------------------------------------------------------+
+31-27 |26-25 |24-20 |19-15 |14-12 | 11-7| 6-2   | 1-0 +
+------------------------------------------------------+
+    offset[11:0]    |00000 |010  | rd  | 11111 | 11  +
+------------------------------------------------------+
```

 - Port OUT:
```
+------------------------------------------------------+
+31-27 |26-25 |24-20 |19-15 |14-12 | 11-7| 6-2   | 1-0 +
+------------------------------------------------------+
+    000000000000    |  rs1 |010  | rd  | 11110 | 11  +
+------------------------------------------------------+
```

 - MUL:
```
+------------------------------------------------------+
+31-27 |26-25 |24-20 |19-15 |14-12 | 11-7| 6-2   | 1-0 +
+------------------------------------------------------+
+100000|  00  | rs2 | rs1  |  000 |   rd  | 01100|  11  +
+------------------------------------------------------+
```

 - DIV:
```
+------------------------------------------------------+
+31-27 |26-25 |24-20 |19-15 |14-12 | 11-7| 6-2   | 1-0 +
+------------------------------------------------------+
+ 11000|  00  | rs2 | rs1  |  000 |   rd  | 01100|  11  +
+------------------------------------------------------+
```


# Operations performed
Following are the operations that this SOC can perform:
 - :heavy_check_mark: AND
 - :heavy_check_mark: OR
 - :heavy_check_mark: ADD
 - :heavy_check_mark: SUB
 - :heavy_check_mark: MUL
 - :heavy_check_mark: DIV
 - :heavy_check_mark: SL
 - :heavy_check_mark: SR
 - :heavy_check_mark: ADDI
 - :heavy_check_mark: LOAD
 - :heavy_check_mark: STORE
 - :heavy_check_mark: BEQ
 - :heavy_check_mark: PORT_IN
 - :heavy_check_mark: PORT_OUT


# Instructions processing flow
 1. Fetch Instruction from Instruction Memory.
 2. Process the instruction from the Decode stage. i.e., read the RS1, RS2, RD or the offset address and the immediate value.
 3. Read the register contents from the register address decoded.
 4. Forward the Decoded data to the ALU stage to perform the required computation on the data.
 5. If a branch instruction is detected, then update the PC and branch to the target address computed by ALU.
 6. If no branch is taken, then read/write the contents from/to the Data Memory.
 7. The result from the above stage is written onto the destination register RD if applicable.
 8. The PC is increemented and the next instruction is fetched from the Instruction Memory.


# Exception scenarios

Exceptions are detected in the following scenarios:
 1. Attempt to Divide_By_Zero while processing DIV instruction.
 2. When a Invalid_Instruction is detected in the Decode stage.
 3. Access to Memory_Out_Of_Bounds when a read/write from/to the Data_Memory/Instruction_Memory. 

# Files for input and output
 1. Instruction_Memory.txt : File that contains the encoded Instructions in the machine language format. The Instruction Memory is initialized with this file contents.
 2. Data_Memory.txt        : File that contains the Data in the machine language format. The Data Memory locations are initialized with this file contents.
 3. Register_Memory.txt    : File that contains the register data in the machine language format. The Registers are initialized with this file contents.
 4. Port_Data.txt          : Data is written to this file to indicate the contents of the Output Port whenever a Port_Out operation is performed.
 5. Updated_Reg_Memory.txt : The final updated values on the registers are stored in this file.
 6. Profile_Stats.txt      : The profiling report of the package.
 7. index.html             : The link to the documentaion generated from doxygen.
