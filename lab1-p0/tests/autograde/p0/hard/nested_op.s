
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $44, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    movl $12, -4(%ebp)
    call eval_input_int
    movl %eax, -8(%ebp)
    movl $2, -12(%ebp)
    movl -12(%ebp), %ecx
    negl %ecx
    movl %ecx, -16(%ebp)
    movl -4(%ebp), %ecx
    movl -16(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -20(%ebp)
    movl -8(%ebp), %ecx
    movl -20(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -24(%ebp)
    movl -4(%ebp), %ecx
    negl %ecx
    movl %ecx, -28(%ebp)
    movl -24(%ebp), %ecx
    movl -28(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -32(%ebp)
    movl -32(%ebp), %ecx
    negl %ecx
    movl %ecx, -36(%ebp)
    movl $2, %ecx
    movl -36(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -40(%ebp)
    movl $3, %ecx
    movl -40(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -44(%ebp)
    movl -44(%ebp), %eax
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
        