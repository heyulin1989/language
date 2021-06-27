        ;; move_string.asm
        %macro prnt 2

        mov rax,1               ;1 = write
        mov rdi,1               ;1 = to stdout
        mov rsi,%1              ;
        mov rdx,%2
        syscall
        mov rax,1
        mov rdi,1
        mov rsi,NL
        mov rdx,1

        %endmacro

        section .data
        length equ 95
        NL db 0xa
        string1 db "my_string of ASCII: "
        string2 db 10, "my_string of zeros: "
        string3 db 10, "my_string of ones: "
        string4 db 10, "again my_string of ASCII: "
        string5 db 10, "copy my_string to other_string. "
        string6 db 10, "reverse copy my_string to other_string."

        section .bss
        my_string resb length
        other_string resb length

        section .text
        global main
main:
        push rbp
        mov rbp,rsp
        ;; ----------------------------------------------
        ;; fill the string with printable ascii chararcters
        prnt string1,18

        mov rax,32
        mov rdi,my_string
        mov rcx,length
        
str_loop1:
        mov byte[rdi],al        ;the simple method
        inc rdi
        inc al
        loop str_loop1
        prnt my_string,length
        
        ;; file the string with ascii 0's
        prnt string2,20
        mov rax,48
        mov rdi,my_string
        mov rcx,length
str_loop2:
        stosb                   
        loop str_loop2
        prnt my_string,length
        ;; ----------------------------------------------
        ;; file the string with ascii 1's
        prnt string3,20
        mov rax,49
        mov rdi,my_string
        mov rcx,length
        rep stosb               ;no inc rdi and no loop need anymore
        prnt my_string,length

        ;; ----------------------------------------------
        ;; fill the string again with printable ascii characters
        prnt string4,26
        mov rax,32
        mov rdi,my_string
        mov rcx,length
str_loop3:
        mov byte[rdi],al        ;the simple method
        inc rdi
        inc al
        loop str_loop3
        prnt my_string, length

        ;; ----------------------------------------------
        ;; copy my_string to other_string
        prnt string5, 32
        mov rsi,my_string       ;rsi source
        mov rdi,other_string    ;rdi destination
        mov rcx,length
        rep movsb
        prnt other_string,length

        ;; ----------------------------------------------
        ;; reverse copy my_string to other_string
        prnt string6,40
        mov rax,48              ;clear other_string
        mov rdi,other_string
        mov rcx,length
	rep stosb
        lea rsi,[my_string+length-4]
        lea rdi,[other_string+length]
        mov rcx,27              ;copy only 27-1 characters
	;; MOVSB 的英文是 move string byte，意思是搬移一个字节，它是把 DS:SI 所指地址的一个字节搬移到 ES:DI 所指的地址上，搬移后原来的内容不变，但是原来 ES:DI 所指的内容会被覆盖而且在搬移之后 SI 和 DI 会自动地指向下一个要搬移的地址。 一般而言，通常程序设计师一般并不会只搬一个字节，通常都会重复许多次，如果要重复的话，就得把重复次数 ( 也就是字串长度 ) 先记录在 CX 寄存器，并且在 MOVSB 之前加上 REP 指令，REP 是重复 (repeat) 的意思。这种写法很是奇怪，一般而言汇编语言源文件的每一行都只有一个指令，但 REP MOVSB 却可以在同一行写两个指令，当然分开写也是一样的。通过标志位DF控制移动的方向，CLD（CLear Direction flag）则是清方向标志位，也就是使DF的值为0，在执行串操作时，使地址按递增的方式变化，这样便于调整相关段的的当前指针。这条指令与STD（SeT Direction flag）的执行结果相反，即置DF的值为1。
	;; 例如:
	;; MOV CX ,100
	;; LEA SI,FIRST
	;; LEA DI,SECOND
	;; REP MOVSB
        ;; 以上程序段的功能是从缓冲区FIRST传送100个字节到SECOND缓冲区.
        
        std                     ;std sets DF,cld clears DF
        rep movsb
        prnt other_string,length


        
        prnt NL, 1
        mov rsp,rbp
        pop rbp
        ret
        
