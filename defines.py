BINARY_FORMAT = 2           # 
REG_CNT = 32                # Number of registers used
INPUT_PORT_CNT = 32         # Number of Input ports in the system
OUTPUT_PORT_CNT = 32        # Number of Output ports in the system

DATA_MEMORY_CNT = 1024      # Size of the Data Memory
INST_MEMORY_CNT = 22        # Size of the Instruction Memory


# Opcode used for each instruction Type
IMMEDIATE_TYPE = "00100"
REGISTER_REGISTER_TYPE = "01100"
LOAD_TYPE = "00000"
STORE_TYPE = "01000"
BRANCH_TYPE = "11000"
PORT_IN_TYPE = "11111"
PORT_OUT_TYPE = "11110"


# Opcode used for each operation Type
AND = "0000000111"
OR = "0000000110"
ADD = "0000000000"
SUB = "0100000000"
MUL = "1000000000"
DIV = "1100000000"
SL = "0000000001"
SR = "0100000101"

# File Names
DATA_MEM_FILE = "Data_Memory.txt"
INST_MEM_FILE = "Instruction_Memory.txt"
REG_FILE_NAME = "Register_Memory.txt"