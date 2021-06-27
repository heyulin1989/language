strings:strings.o
	gcc -o strings strings.o -ggdb -no-pie
strings.o: strings.asm
	nasm -f elf64 -g -F dwarf strings.asm -l strings.lst
