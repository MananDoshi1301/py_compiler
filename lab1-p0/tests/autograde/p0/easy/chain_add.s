
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $16, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    movl $1, %ecx
    movl $2, %eax
    addl %ecx, %eax
    movl %eax, -4(%ebp)
    movl -4(%ebp), %ecx
    movl $3, %eax
    addl %ecx, %eax
    movl %eax, -8(%ebp)
    movl -8(%ebp), %ecx
    movl $4, %eax
    addl %ecx, %eax
    movl %eax, -12(%ebp)
    movl -12(%ebp), %ecx
    movl $5, %eax
    addl %ecx, %eax
    movl %eax, -16(%ebp)
    movl -16(%ebp), %eax
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
        