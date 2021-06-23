	;; stack.asm
	extern printf
	section  .data
	strng db "ABCDE",0
	strnglen equ $ - strng - 1	;stringlength without 0
	fmt1 db "The original string: %s", 10, 0
	fmt2 db "The reversed string: %s", 10, 0

	section .bss
	section .text
	global main
main:
	push rbp
	mov rbp,rsp
	;; print the original string
	mov rdi,fmt1
	mov rsi,strng
	mov rax,0
	call printf
	
	;; push the string char per char on the stack
	xor rax,rax
	mov rbx,strng				;address of strng in rbx
	mov rcx,strnglen			;length in rcx counter
	mov r12,0					;use r12 as pointer
pushLoop:
	mov al,byte[rbx+r12]		;mov char into rax
	push rax					;push rax on the stack
	inc r12						;increase char pointer with 1
	loop pushLoop				;continue loop
	;; pop the string char per char from the stack
	;; this will reverse the original string
	mov rbx,strng				;address of strng in rbx
	mov rcx,strnglen			;length in rcx counter
	mov r12,0
popLoop:
	pop rax						;pop a char from the stack
	mov byte[rbx+r12],al		;move the char into string
	inc r12						;increase char pointer with 1
	loop popLoop				;continue loop
	mov byte[rbx+r12],0			;terminate string with 0
	;; print the reversed string
	mov rdi,fmt2
	mov rsi,strng
	mov rax,0
	call printf

	mov rsp,rbp
	pop rbp
	ret
