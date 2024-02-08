
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $36, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    call eval_input_int
    movl %eax, -4(%ebp)
    movl -4(%ebp), %ecx
    negl %ecx
    movl %ecx, -8(%ebp)
    movl -8(%ebp), %eax
    movl %eax, -28(%ebp)
    movl -28(%ebp), %ecx
    movl $23, %eax
    addl %ecx, %eax
    movl %eax, -16(%ebp)
    movl -16(%ebp), %eax
    movl %eax, -20(%ebp)
    call eval_input_int
    movl %eax, -24(%ebp)
    movl -24(%ebp), %eax
    movl %eax, -28(%ebp)
    movl -28(%ebp), %ecx
    movl -20(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -32(%ebp)
    movl -32(%ebp), %eax
    movl %eax, -36(%ebp)
    movl -36(%ebp), %eax
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
        