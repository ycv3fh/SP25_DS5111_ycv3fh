import os

os.system("make gainers SRC=yahoo")
os.system("make gainers SRC=wsj")
os.system("mv yahoo_gainers* data_collected")
os.system("mv wsj_gainers* data_collected")
os.system("rm ygainers*")
os.system("rm wsjgainers*")
