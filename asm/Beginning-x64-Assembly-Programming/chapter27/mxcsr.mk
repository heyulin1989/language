mxcsr:mxcsr.o print_mxcsr.o print_hex.o
	gcc -o  mxcsr mxcsr.o print_mxcsr.o print_hex.o -ggdb -no-pie
mxcsr.o: mxcsr.asm
	nasm -f elf64 -g -F dwarf mxcsr.asm -l mxcsr.lst
print_mxcsr.o: print_mxcsr.c
	gcc -c -g print_mxcsr.c
print_hex.o: print_hex.c
	gcc -c -g print_hex.c
