function:function.o
	gcc -o function function.o -ggdb -no-pie
function.o: function.asm
	nasm -f elf64 -g -F dwarf function.asm -l function.lst
