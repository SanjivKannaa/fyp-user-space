bash ./set.sh
echo "set arptables rules"
python3 main.py
bash ./rm.sh
echo "flushed arptables"
