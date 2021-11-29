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

**Source : [ISA](https://msyksphinz-self.github.io/riscv-isadoc/html/rvi.html#ebreak)!**



# Operations performed



# Instructions processing flow




# Exception scenarios




# Files for input and output
