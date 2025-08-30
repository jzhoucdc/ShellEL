#!/usr/bin/python3

import sys
from pwn import *

context(os="linux", arch="amd64", log_level="error")

def usage():
    print(f"Usage: {sys.argv[0]} -E <elf_file>   # 提取shellcode")
    print(f"       {sys.argv[0]} -L <hex_code>   # 加载shellcode")
    print(f"       {sys.argv[0]} -h              # 帮助信息")

if len(sys.argv) < 2 or sys.argv[1] == "-h":
    usage()
    sys.exit(0)

if sys.argv[1] == "-E":
    if len(sys.argv) < 3:
        print("缺少提取的文件路径")
        sys.exit(1)
    file = ELF(sys.argv[2])
    shellcode = file.section(".text")
    print(shellcode.hex())

elif sys.argv[1] == "-L":
    if len(sys.argv) < 3:
        print("缺少shellcode-hex")
        sys.exit(1)
    run_shellcode(unhex(sys.argv[2])).interactive()
