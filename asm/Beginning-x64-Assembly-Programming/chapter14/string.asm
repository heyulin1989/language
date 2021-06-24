	;; string.asm
	extern strlen
	extern printf
	
	section .data
	str1 db "abc",0
	fmt db "strlen %s is %d",10,0
	section .bss
	section .text
	global main
main:
	push rbp
	mov rbp,rsp
	mov rdi,str1
	call strlen
	
	mov rdi, fmt
	mov rsi, str1
	mov rdx, rax
	mov rax, 0
	call printf
	
	leave
	ret
