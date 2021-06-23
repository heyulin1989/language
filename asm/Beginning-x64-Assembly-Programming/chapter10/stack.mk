stack:stack.o
	gcc -o stack stack.o -ggdb -no-pie
stack.o: stack.asm
	nasm -f elf64 -g -F dwarf stack.asm -l stack.lst
