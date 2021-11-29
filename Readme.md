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
 - :heavy_check_mark: ADD


# Instructions processing flow




# Exception scenarios




# Files for input and output
