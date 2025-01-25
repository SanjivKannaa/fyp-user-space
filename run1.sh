#!/bin/bash
clear
arptables -A INPUT -j NFQUEUE --queue-num 69
echo "set arptables input rule"

python3 main1.py

arptables -F
echo "flushed arptables"