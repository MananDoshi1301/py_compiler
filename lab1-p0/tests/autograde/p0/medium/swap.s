
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $20, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    movl $2, -16(%ebp)
    movl $3, -20(%ebp)
    movl -16(%ebp), %eax
    pushl %eax
    call print_int_nl
    addl $4, %esp
    movl -20(%ebp), %eax
    pushl %eax
    call print_int_nl
    addl $4, %esp
    movl -16(%ebp), %eax
    movl %eax, -12(%ebp)
    movl -20(%ebp), %eax
    movl %eax, -16(%ebp)
    movl -12(%ebp), %eax
    movl %eax, -20(%ebp)
    movl -16(%ebp), %eax
    pushl %eax
    call print_int_nl
    addl $4, %esp
    movl -20(%ebp), %eax
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
        