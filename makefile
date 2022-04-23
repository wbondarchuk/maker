#makefile for filename.asm
filename: filename.o
	ld -m elf_i386 filename.o -o filename
filename.o: filename.asm
	nasm -f elf -g -F dwarf filename.asm -l filename.lst
