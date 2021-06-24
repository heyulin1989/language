string: string.o
	gcc -g -o string string.o -no-pie
string.o: string.asm
	nasm -f elf64 -g -F dwarf string.asm -l string.lst
