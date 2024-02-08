
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $52, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    movl $2, -4(%ebp)
    movl -4(%ebp), %ecx
    movl $1, %eax
    addl %ecx, %eax
    movl %eax, -8(%ebp)
    movl -8(%ebp), %ecx
    movl $2, %eax
    addl %ecx, %eax
    movl %eax, -12(%ebp)
    movl -12(%ebp), %ecx
    movl $3, %eax
    addl %ecx, %eax
    movl %eax, -16(%ebp)
    movl -16(%ebp), %ecx
    movl $4, %eax
    addl %ecx, %eax
    movl %eax, -20(%ebp)
    movl -20(%ebp), %ecx
    movl $5, %eax
    addl %ecx, %eax
    movl %eax, -24(%ebp)
    movl -24(%ebp), %ecx
    movl $6, %eax
    addl %ecx, %eax
    movl %eax, -28(%ebp)
    movl -28(%ebp), %ecx
    movl $7, %eax
    addl %ecx, %eax
    movl %eax, -32(%ebp)
    movl -32(%ebp), %ecx
    movl $8, %eax
    addl %ecx, %eax
    movl %eax, -36(%ebp)
    movl -36(%ebp), %ecx
    movl $9, %eax
    addl %ecx, %eax
    movl %eax, -40(%ebp)
    movl -40(%ebp), %ecx
    movl $10, %eax
    addl %ecx, %eax
    movl %eax, -44(%ebp)
    movl -44(%ebp), %ecx
    movl $11, %eax
    addl %ecx, %eax
    movl %eax, -48(%ebp)
    movl -48(%ebp), %ecx
    movl $12, %eax
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
        