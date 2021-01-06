from .config import *


class Inst(object):
   # ADD   = BitPat("b0000000??????????000?????0110011")
   ADD   = BitPat("0000000??????????000?????0110011")
   SUB   = BitPat("0100000??????????000?????0110011")
   AND   = BitPat("0000000??????????111?????0110011")
   OR    = BitPat("0000000??????????110?????0110011")
   XOR   = BitPat("0000000??????????100?????0110011")

   ADDI  = BitPat("?????????????????000?????0010011")
   ANDI  = BitPat("?????????????????111?????0010011")
   ORI   = BitPat("?????????????????110?????0010011")
   XORI  = BitPat("?????????????????100?????0010011")

   SLL   = BitPat("0000000??????????001?????0110011")
   SRL   = BitPat("0000000??????????101?????0110011")
   SRA   = BitPat("0100000??????????101?????0110011")

   SLLI  = BitPat("0000000??????????001?????0010011")
   SRLI  = BitPat("0000000??????????101?????0010011")
   SRAI  = BitPat("0100000??????????101?????0010011")

   SLT   = BitPat("0000000??????????010?????0110011")
   SLTU  = BitPat("0000000??????????011?????0110011")
   SLTI  = BitPat("?????????????????010?????0010011")
   SLTIU = BitPat("?????????????????011?????0010011")

   LW    = BitPat("?????????????????010?????0000011")
   LH    = BitPat("?????????????????001?????0000011")
   LB    = BitPat("?????????????????000?????0000011")
   LBU   = BitPat("?????????????????100?????0000011")
   LHU   = BitPat("?????????????????101?????0000011")

   SW    = BitPat("?????????????????010?????0100011")
   SH    = BitPat("?????????????????001?????0100011")
   SB    = BitPat("?????????????????000?????0100011")

   BEQ   = BitPat("?????????????????000?????1100011")
   BNE   = BitPat("?????????????????001?????1100011")
   BLT   = BitPat("?????????????????100?????1100011")
   BGE   = BitPat("?????????????????101?????1100011")
   BLTU  = BitPat("?????????????????110?????1100011")
   BGEU  = BitPat("?????????????????111?????1100011")

   JAL   = BitPat("?????????????????????????1101111")
   JALR  = BitPat("?????????????????000?????1100111")

   AUIPC = BitPat("?????????????????????????0010111")

   LUI   = BitPat("?????????????????????????0110111")

   NOP   = BitPat("00000000000000000000000000010011")

   # csr add start
   # CSR instructions

   CSRRW  = BitPat("?????????????????001?????1110011")
   CSRRS  = BitPat("?????????????????010?????1110011")
   CSRRC  = BitPat("?????????????????011?????1110011")
   CSRRWI = BitPat("?????????????????101?????1110011")
   CSRRSI = BitPat("?????????????????110?????1110011")
   CSRRCI = BitPat("?????????????????111?????1110011")
   MRET   = BitPat("00110000001000000000000001110011")

   # initial void
   VOID   = BitPat("00000000000000000000000000000000")
   # csr add end

