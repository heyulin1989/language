        ;; console1.asm

section .data
	msg1       db    "Hello, World!",10,0
        msg1len    equ   $-msg1-1
        msg2       db    "Your turn: ",0
        msg2len    equ   $-msg2-1
        msg3       db    "You answered: ",0
        msg3len    equ   $-msg3-1
        inputlen equ     10   ;length of inputbuffer
section .bss
        input resb inputlen+1 ;provide space for ending 0
section .text
        global main
main:
        push rbp
        mov rbp,rsp

        mov rsi, msg1       ; print first string
        mov rdx, msg1len
        call prints
        
        mov rsi,msg2
        mov rdx,msg2len
        call prints

        mov rsi,input
        mov rdx,inputlen
        call reads

	mov rsi,msg3
        mov rdx,msg3len
        call prints

        mov rsi,input           ;print the inputbuffer
        mov rdx,inputlen        ;length of inputbuffer
        call prints
        
        mov rsp,rbp
        pop rbp
        ret
        ;; ------------------------------------------------
prints:
        push rbp
        mov rbp,rsp
        ;; rsi contains address of string
        ;; rdx contains leave of string
        mov rax,1               ;1 = write
        mov rdi,0               ;0 = stdout
        syscall

        leave
        ret
        
        ;; ------------------------------------------------
reads:
        push rbp
        mov rbp,rsp
        ;; rsi contains address of the inputbuffer
        ;; rdi contains length of the inputbuffer
        mov rax,0               ;0 = read
        mov rdi,1               ;1 = stdin
        syscall
        
        leave
        ret
