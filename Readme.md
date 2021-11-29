# Emulated SOC Design

This project aims at providing the simulated functionality of the SOC when the assembly instructions (i.e., encoded in 1's and 0's) are to be processed.
The choice of the Instruction Set Architecture(ISA) is the RV32I. It is a 32-bit instruction set with each instruction, data and memory of size 32-bits.
Hence, the memory here is word addressable.


# Top level view of the design and the SOC components
'''
+-----------------------------------------------------------------------------------------------+
| +-------+                                                                                     |
| |       |                                                                                     |
| |   PC  |     +-----------------------------------------+                                     |
| |       |     |                   MEMORY                |                                     |
|	+-------+			|										  |								|
|						|	+-------------+		+-------------+	  |								|
|						|	|    INST     |		|    DATA     |	  |								|
|	+--------+			|	|   MEMORY    |		|   MEMORY    |	  |				+--------+		|
|	|        |			|	+-------------+     +-------------+   |     		|        |		|
|	|        |			|	|             |		|             |	  |				|		 |		|
|	|        |			|	|             |		|             |	  |				|        |		|
|	|        |			|	|             |		|             |	  |				|        |		|
|	|        |			|	|             |		|             |	  |				|        |		|
|	|   IN   |			|	|             |		|             |	  |				|   OUT  |		|
|	|  PORT  |			|	|             |		|             |	  |				|  PORT  |		|
|	|        |			|	|             |		|             |	  |				|        |		|
|	|        |			|	|             |		|             |	  |				|        |		|
|	|        |			|	|             |		|             |	  |				|        |		|
|	|        |			|	|             |		|             |	  |				|        |		|
|	|        |			|	|             |		|             |	  |				|		 |		|
|	+--------+			|	|             |		|             |	  |				+--------+		|
|						|	|             |		|             |	  |								|
|						|	|             |		|             |	  |								|
|						|	+-------------+		+-------------+	  |								|
|						|										  |								|
|						+-----------------------------------------+								|
|																								|
|																								|
|	+-------------+			          +-------------+				        +-------------+		|
|	|     ALU     |			          |   DECODE    |				        |  REGISTERS  |		|
|	|-------------|			          |-------------|	        	        |-------------|		|
|	|             |			          |             |				        |             |		|
|	|             |			          |             |				        |             |		|
|	|             |			          |             |				        |             |		|
|	|             |			          |             |				        |             |		|
|	+-------------+			          +-------------+				        +-------------+		|
|																								|
|																								|
+-----------------------------------------------------------------------------------------------+
'''



# Instruction encoding and format




# Operations performed



# Instructions processing flow




# Exception scenarios




# Files for input and output
