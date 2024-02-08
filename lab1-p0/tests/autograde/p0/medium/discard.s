
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl $8, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        
    movl $1, -4(%ebp)
    movl $2, -8(%ebp)

    popl %edi 
    popl %esi
    popl %ebx
    movl $0, %eax 
    movl %ebp, %esp
    popl %ebp
    ret
        