
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $16, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    call eval_input_int
    movl %eax, -4(%ebp)
    call eval_input_int
    movl %eax, -8(%ebp)
    movl -4(%ebp), %ecx
    movl -8(%ebp), %eax
    addl %ecx, %eax
    movl %eax, -12(%ebp)
    call eval_input_int
    movl %eax, -16(%ebp)

    popl %edi 
    popl %esi
    popl %ebx
    movl $0, %eax 
    movl %ebp, %esp
    popl %ebp
    ret
        