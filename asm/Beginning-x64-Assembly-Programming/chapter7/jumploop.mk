jumploop:jumploop.o
	gcc -o jumploop jumploop.o -ggdb -no-pie
jumploop.o: jumploop.asm
	nasm -f elf64 -g -F dwarf jumploop.asm -l jumploop.lst