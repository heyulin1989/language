fcalc:fcalc.o
	gcc -o fcalc fcalc.o -ggdb -no-pie
fcalc.o: fcalc.asm
	nasm -f elf64 -g -F dwarf fcalc.asm -l fcalc.lst
