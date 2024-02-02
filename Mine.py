from BlockChain.block_chain import Block_Chain as bc
from msvcrt import kbhit, getch
from random import randint
from time import perf_counter
from os.path import isfile
from os import mkdir

import os
import json

# Checking if accounts exist
is_file = isfile(r"C:\Local\account.json")
if not is_file:
    mkdir(r"C:\Local")
    Names = [
        'Ben',
        'Brandon',
        'Dawn',
        'Jacob',
        'Gwen',
        'Mark',
        'Grammy'
    ]
    names = {
        'Ben': {"Amount": 0, "Coin Bin": []},
        'Brandon': {"Amount": 0, "Coin Bin": []},
        'Dawn': {"Amount": 0, "Coin Bin": []},
        'Jacob': {"Amount": 0, "Coin Bin": []},
        'Gwen': {"Amount": 0, "Coin Bin": []},
        'Mark': {"Amount": 0, "Coin Bin": []},
        'Grammy': {"Amount": 0, "Coin Bin": []}
    }
else:
    Names = [
        'Ben',
        'Brandon',
        'Dawn',
        'Jacob',
        'Gwen',
        'Mark',
        'Grammy'
    ]
    file = open(r"C:\Local\account.json", 'r')
    names=json.load(file)
    file.close()
#

is_file1 = isfile(r"C:\Local\block_chain.json")
is_file2 = isfile(r"C:\Local\index.txt")
if not is_file1 and not is_file2:
    # Objects
    # - Block Chain
    block_chain = bc()
    #
else:
    file = open(r"C:\Local\block_chain.json", 'r')
    chain = json.load(file)
    file.close()
    file = open(r"C:\Local\index.txt", 'r')
    index = file.read()
    file.close()
    # Objects
    # - Block Chain
    block_chain = bc(chain=chain, index=int(index))
    #
    
    # Clear Screen
    os.system('cls')

name_index=0
while True:

    start = perf_counter()


    index, coin_ID = block_chain.Construct_Block(Name=Names[name_index])
    name_index+=1

    names[Names[name_index-1]]["Coin Bin"].append(coin_ID)
    names[Names[name_index-1]]["Amount"]+=1

    stealing = randint(1, 1000)

    if stealing <= 10:
        names[Names[name_index-1]]["Coin Bin"].pop()
        names[Names[name_index-1]]["Amount"]-=1

        block_chain.chain.pop()
        block_chain.index-=1

    if name_index == 7:
        name_index=0

    if kbhit():
        key = getch()

        if key == b'p':
            print()
            break

    end = perf_counter()

    print(f"Coins Mined: {index}", end='\r')


file = open(r"C:\Local\index.txt", 'w')
file.write(str(block_chain.index))
file.close()

file = open(r"C:\Local\block_chain.json", 'w')
file.write(json.dumps(block_chain.chain))
file.close()

file = open(r"C:\Local\account.json", 'w')
file.write(json.dumps(names))
file.close()