move_string:move_string.o
	gcc -o move_string move_string.o -ggdb -no-pie
move_string.o: move_string.asm
	nasm -f elf64 -g -F dwarf move_string.asm -l move_string.lst
