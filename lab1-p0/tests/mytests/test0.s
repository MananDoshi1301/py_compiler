
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $4, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    movl $1, %ecx
    movl $2, %eax
    addl %ecx, %eax
    movl %eax, -4(%ebp)
    movl -4(%ebp), %eax
    pushl %eax
    call print_int_nl
    addl $4, %esp

    popl %edi 
    popl %esi
    popl %ebx
    movl $0, %eax 
    movl %ebp, %esp
    popl %ebp
    ret
        