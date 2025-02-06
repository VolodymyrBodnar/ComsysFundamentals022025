sudo apt update
sudo apt install nasm gcc -y


nasm -f elf64 hello.asm -o hello.o
gcc hello.o -o hello
./hello


nasm -f elf64 multiply.asm -o multiply.o
gcc multiply.o -o multiply -no-pie -lc
./multiply