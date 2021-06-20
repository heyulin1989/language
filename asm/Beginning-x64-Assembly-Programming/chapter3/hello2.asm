    ;; hello.asm
    section .data
    msg db "hello, worldg",0
    NL  db 0xa    ; ascii code for new line
    section .bss
    section .text
    global main
main:
    mov rax, 1                     ; 1 = write
    mov rdi, 1                     ; 1 = to stdout
    mov rsi, msg                   ; string to display in rsi
    mov rdx, 12                    ; length of the string, without 0
    syscall                        ; display the string
    mov rax, 1                     ; 1 = write
    mov rdi, 1                     ; 1 = to stdout
    mov rsi, NL                    ; string to display in rsi
    mov rdx, 1                     ; length of the string, without 0
    syscall                        ; display the string
    mov rax, 60                    ; 60 =
    exit
    mov rdi, 2                     ; 0 = success exit code
    syscall                     ; quit
