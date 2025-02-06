section .data
    result_msg db "Result: ", 0
    result_len equ $ - result_msg

section .bss
    result resb 4   ; Буфер для результату

section .text
    global main
main:

    mov rax, 2      ; Завантажуємо 2 в rax
    mov rbx, 2      ; Завантажуємо 2 в rbx
    mul rbx         ; rax = rax * rbx (тобто 2 * 2)

    ; Вивід результату через printf
    mov rdi, result_msg
    mov rsi, rax
    syscall

    ; Завершення програми
    mov rax, 60
    xor rdi, rdi
    syscall
