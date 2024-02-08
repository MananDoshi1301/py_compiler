
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $28, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    movl $1, -4(%ebp)
    movl $2, -8(%ebp)
    movl -4(%ebp), %ecx
    movl -8(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -12(%ebp)
    movl -12(%ebp), %eax
    movl %eax, -16(%ebp)
    movl -8(%ebp), %ecx
    movl -16(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -20(%ebp)
    movl -20(%ebp), %eax
    movl %eax, -24(%ebp)
    movl -16(%ebp), %ecx
    movl -24(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -28(%ebp)
    movl -28(%ebp), %eax
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
        