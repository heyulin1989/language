aligned:aligned.o
	gcc -o aligned aligned.o -ggdb -no-pie
aligned.o: aligned.asm
	nasm -f elf64 -g -F dwarf aligned.asm -l aligned.lst
