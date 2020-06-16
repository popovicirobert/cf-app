#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
WHITE='\033[1;37m'

task_id=$1
file_path=$2

current_path=$PWD
cd $file_path

main_file='./main.cpp'
main_exe='./main'
in_file="./$task_id.in"
out_file="./$task_id.out"
tests_path='./tests'

echo -e "\nCompiling file..."
g++ -std=c++17 -DHOME -O2 $main_file -o $main_exe

if [ "$?" -ne "0" ]; then
	echo "Compilation failed"
	exit 1
else
	echo -e "Compilation successfull\n"
fi

echo "Checking tests..."
i=0

while [ -f $tests_path"/input$i.txt" ]; do

	input=$tests_path"/input$i.txt"
	output=$tests_path"/output$i.txt"
	
	cp $input $in_file

	timeout 2s $main_exe

	if [ "$?" -ne "0" ]; then
		echo -e "Test $i ${RED}TLE${WHITE}\n"
		exit 1
	elif diff -qBZ $out_file $output >/dev/null; then
		echo -e "Test $i ${GREEN}OK${WHITE}"
	else
		echo -e "Test $i ${RED}WA${WHITE}\n"
		exit 1
	fi

	i=$((i + 1))

done

echo ""
#echo -e "${GREEN}Pretests passed${WHITE}\n"

rm $main_exe
cd $current_path
