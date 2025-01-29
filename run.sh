#!/bin/bash
clear
# INPUT
arptables -A INPUT -m mac --mac-source 02:42:ac:11:00:02 -j ACCEPT
arptables -A INPUT -j NFQUEUE --queue-num 1

# OUTPUT
arptables -A OUTPUT -m mac --mac-source 02:42:ac:11:00:03 -j ACCEPT
arptables -A OUTPUT -j NFQUEUE --queue-num 2
echo "set arptables input rule"

docker-compose up -d
lazydocker