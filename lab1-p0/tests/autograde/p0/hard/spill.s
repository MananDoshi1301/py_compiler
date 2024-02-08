
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $52, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    movl $1, -4(%ebp)
    movl $2, -8(%ebp)
    movl $3, -12(%ebp)
    movl $23, -16(%ebp)
    movl $2, -20(%ebp)
    movl -20(%ebp), %ecx
    negl %ecx
    movl %ecx, -24(%ebp)
    movl -24(%ebp), %eax
    movl %eax, -28(%ebp)
    movl $12, -32(%ebp)
    movl -4(%ebp), %ecx
    movl -8(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -36(%ebp)
    movl -36(%ebp), %ecx
    movl -12(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -40(%ebp)
    movl -40(%ebp), %ecx
    movl -16(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -44(%ebp)
    movl -44(%ebp), %ecx
    movl -28(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -48(%ebp)
    movl -48(%ebp), %ecx
    movl -32(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -52(%ebp)
    movl -52(%ebp), %eax
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
        