#!/usr/bin/env python3

# import bittensor as bt
from bittensor import subtensor
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()
coldkeys = os.getenv('COLDKEYS').split(",")
# Subnetworks to scan
sns = os.getenv('SNS').split(",")

# try:
#     subtensor = subtensor(network='ws://localhost:9944')
# except Exception as e:
#     print("An unexpected error occurred:", e)
# else:
#     subtensor = subtensor(network='finney')
    
subtensor = subtensor(network='finney')

green_ball_code = "\U0001F7E2"
red_ball_code = "\U0001F534"
yellow_ball_code = "\U0001F7E1"

def get_bittensor_info():
    output = ''
    for sn in sns:
        metagraph = subtensor.metagraph(sn)
        neurons = pd.DataFrame(metagraph.neurons)
        sorted_neurons = neurons.sort_values(by='emission', ascending=False).reset_index(drop=False)
        sorted_neurons.insert(0, 'RANK', range(len(sorted_neurons)))
        my_neurons = sorted_neurons.query(f'coldkey == "{coldkeys[0]}"')
        qty = len(my_neurons) 
        output += f'##### Nodes rank for SN{sn}. Qty ({qty}) ######\n'
        for index, my_neuron in my_neurons.iterrows():
            balloon = set_balloon_color(my_neuron["RANK"])
            output += f'{balloon} UID {my_neuron["uid"]} has position {my_neuron["RANK"]}\n'
        print('\n')
    return output

def set_balloon_color(rank):
    if rank < 100:
        return green_ball_code
    elif rank < 200:
        return yellow_ball_code
    else:
        return red_ball_code

