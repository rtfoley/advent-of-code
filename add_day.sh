#! /bin/bash  

if [ "$#" -eq 2 ]; then
    mkdir -p "$1/day$2"
    if [ $? -eq 0 ]; then
        cp day_template/day.py "$1/day$2/day$2.py"
        cp day_template/test.py "$1/day$2/test.py"
        touch "$1/day$2/input.txt"
    fi
else
    mkdir -p "day$1"
    if [ $? -eq 0 ]; then
        cp ../day_template/day.py "day$1/day$1.py"
        cp ../day_template/test.py "day$1/test.py"
        touch "day$1/input.txt"
    fi
fi