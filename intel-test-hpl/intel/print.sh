#!/bin/bash

python ./py/n.py > temp.txt

python ./py/nb.py >> temp.txt

python ./py/pq.py >> temp.txt

cat temp.txt | tr '\n' ' ' | sed 's/ $//' > script.txt

rm temp.txt