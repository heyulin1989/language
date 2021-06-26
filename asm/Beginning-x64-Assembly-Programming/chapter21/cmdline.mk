cmdline:cmdline.o
	gcc -o cmdline cmdline.o -ggdb -no-pie
cmdline.o:cmdline.asm
	nasm -f elf64 -g -F dwarf cmdline.asm -l cmdline.lst

