betterloop:betterloop.o
	gcc -o betterloop betterloop.o -ggdb -no-pie
betterloop.o: betterloop.asm
	nasm -f elf64 -g -F dwarf betterloop.asm -l betterloop.lst
