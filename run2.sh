#!/bin/bash
clear
arptables -A OUTPUT -j NFQUEUE --queue-num 2
echo "set arptables output rule"

python3 main2.py

arptables -F
echo "flushed arptables"