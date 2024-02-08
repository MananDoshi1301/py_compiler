
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $112, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    call eval_input_int
    movl %eax, -4(%ebp)
    movl $1, %ecx
    movl -4(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -8(%ebp)
    movl -8(%ebp), %eax
    movl %eax, -12(%ebp)
    movl -12(%ebp), %ecx
    movl -12(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -16(%ebp)
    movl -16(%ebp), %eax
    movl %eax, -20(%ebp)
    movl -20(%ebp), %ecx
    movl -20(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -24(%ebp)
    movl -24(%ebp), %eax
    movl %eax, -28(%ebp)
    movl -28(%ebp), %ecx
    movl -28(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -32(%ebp)
    movl -32(%ebp), %eax
    movl %eax, -36(%ebp)
    movl -36(%ebp), %ecx
    movl -36(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -40(%ebp)
    movl -40(%ebp), %eax
    movl %eax, -44(%ebp)
    movl -44(%ebp), %ecx
    movl -44(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -48(%ebp)
    movl -48(%ebp), %eax
    movl %eax, -52(%ebp)
    movl -52(%ebp), %ecx
    movl -52(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -56(%ebp)
    movl -56(%ebp), %eax
    movl %eax, -60(%ebp)
    movl -60(%ebp), %ecx
    movl -60(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -64(%ebp)
    movl -64(%ebp), %eax
    movl %eax, -68(%ebp)
    movl -68(%ebp), %ecx
    movl -68(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -72(%ebp)
    movl -72(%ebp), %eax
    movl %eax, -76(%ebp)
    movl -12(%ebp), %ecx
    movl -20(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -80(%ebp)
    movl -80(%ebp), %ecx
    movl -28(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -84(%ebp)
    movl -84(%ebp), %ecx
    movl -36(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -88(%ebp)
    movl -88(%ebp), %ecx
    movl -44(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -92(%ebp)
    movl -92(%ebp), %ecx
    movl -52(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -96(%ebp)
    movl -96(%ebp), %ecx
    movl -60(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -100(%ebp)
    movl -100(%ebp), %ecx
    movl -68(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -104(%ebp)
    movl -104(%ebp), %ecx
    movl -76(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -108(%ebp)
    movl -108(%ebp), %eax
    movl %eax, -112(%ebp)
    movl -60(%ebp), %eax
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
        