import os
os.system("make gainers SRC=yahoo")
os.system("make gainers SRC=wsj")
os.system("mv yahoo_gainers* data_collected")
os.system("mv wsj_gainers* data_collected")
os.system("make clean_ygainers")
os.system("make clean_wsjgainers")
