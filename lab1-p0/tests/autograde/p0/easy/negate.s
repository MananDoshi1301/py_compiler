
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $12, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    movl $2, -4(%ebp)
    movl -4(%ebp), %ecx
    negl %ecx
    movl %ecx, -8(%ebp)
    movl -8(%ebp), %eax
    movl %eax, -12(%ebp)
    movl -4(%ebp), %eax
    pushl %eax
    call print_int_nl
    addl $4, %esp
    movl -12(%ebp), %eax
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
        