
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $32, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    movl $23, -4(%ebp)
    movl $6, -8(%ebp)
    movl -8(%ebp), %ecx
    negl %ecx
    movl %ecx, -12(%ebp)
    movl -12(%ebp), %eax
    movl %eax, -16(%ebp)
    movl $12, -20(%ebp)
    movl -4(%ebp), %ecx
    movl -16(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -24(%ebp)
    movl -24(%ebp), %ecx
    movl -20(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -28(%ebp)
    movl -28(%ebp), %eax
    pushl %eax
    call print_int_nl
    addl $4, %esp
    movl -16(%ebp), %ecx
    movl -20(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -32(%ebp)
    movl -32(%ebp), %eax
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
        