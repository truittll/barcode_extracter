__author__= 'truittll'

import numpy as np
import pandas as pd
import random
import csv
import sys

'''my monte carlo script-mainly for practice'''

def MC_sim(sample, n_min, n_max, inc, threshold):
    sample_length = sample.size
    proportioned_pool= []
    bar = list(sample.index.values)
    for i in xrange(0,sample_length):
        temp = [bar[i]]*sample.iat[i,0]
        proportioned_pool.extend(temp)

    all_simulations = [[0,0]]
    for n in xrange(int(n_min), int(n_max)+int(inc), int(inc)):
        success_track = 0
        for trial in range(100):
            temp_list = np.random.choice(proportioned_pool, n)
            if (len(temp_list) - len(set(temp_list)) <= float(threshold)*len(temp_list)):
                success_track += 1
        success_track = float(success_track)        
        all_simulations.append([n,success_track/100.])
        data = pd.DataFrame(data = all_simulations)
    return data

if __name__ == "__main__":

    file_name = sys.argv[1]
    min_cell = sys.argv[2]
    max_cell = sys.argv[3]
    inc_cell = sys.argv[4]
    p_value = sys.argv [5]
    new_file_name = sys.argv[6]

    sample_file = pd.read_csv(file_name,delimiter=r"\s+")

    MC_data = MC_sim(sample_file , min_cell, max_cell, inc_cell, p_value)

    MC_data.to_csv(new_file_name,header=False)


    
