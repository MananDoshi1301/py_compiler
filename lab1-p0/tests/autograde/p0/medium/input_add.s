
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $64, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    call eval_input_int
    movl %eax, -4(%ebp)
    movl -4(%ebp), %eax
    movl %eax, -8(%ebp)
    call eval_input_int
    movl %eax, -12(%ebp)
    movl -12(%ebp), %ecx
    movl -8(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -16(%ebp)
    movl -16(%ebp), %eax
    movl %eax, -20(%ebp)
    call eval_input_int
    movl %eax, -24(%ebp)
    movl -24(%ebp), %ecx
    movl -20(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -28(%ebp)
    movl -28(%ebp), %eax
    movl %eax, -32(%ebp)
    call eval_input_int
    movl %eax, -36(%ebp)
    movl -36(%ebp), %ecx
    movl -32(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -40(%ebp)
    movl -40(%ebp), %eax
    movl %eax, -44(%ebp)
    movl -8(%ebp), %ecx
    movl -20(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -48(%ebp)
    movl -48(%ebp), %ecx
    movl -32(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -52(%ebp)
    movl -52(%ebp), %ecx
    movl -44(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -56(%ebp)
    call eval_input_int
    movl %eax, -60(%ebp)
    movl -56(%ebp), %ecx
    movl -60(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -64(%ebp)
    movl -64(%ebp), %eax
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
        