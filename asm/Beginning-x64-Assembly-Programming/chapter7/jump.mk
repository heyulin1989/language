jump:jump.o
	gcc -o jump jump.o -ggdb -no-pie
jump.o: jump.asm
	nasm -f elf64 -g -F dwarf jump.asm -l jump.lst
