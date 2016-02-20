.globl  main
main:
    jmp  L2
L1:
    popl %ecx
    movl $0x4,%eax
    movl $0x1,%ebx
    movl $0xd,%edx
    int  $0x80
    xorl %eax,%eax
    movl %eax,%ebx
    inc  %eax
    int  $0x80
L2:
    call L1
    .string "Hello World!\n"

