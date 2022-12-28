# Developer : Al Sabawi

import sys
import numpy as np
import time
import array as arr

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            arg_in = float(sys.argv[1])
        except ValueError:
            print('Argument',sys.argv[1], 'is not a float data type. Try again.')
            quit()

        bias = float(sys.argv[1])
        print('Bias = ',bias)
    else:
        print ( '*** Usage:',sys.argv[0], '<bias factor as fraction between 0.0 to 1.0>\n')
        quit()

max_flips = 100000
states_num = 2
#flip_stat = arr.array('i',(0 for i in range(0,states_num)))
np.random.seed(int(time.time()))

def numaric_array(atype,index_start,index_end,init_value):
    return arr.array(atype,(init_value for i in range(index_start,index_end)))

def generate_random_number():
    return np.random.random()

def generate_bias_outcome(b=0.5):
    if generate_random_number() < b:
        return 1
    else:
        return 0

print('Testing a coin flip', max_flips,'times. \nResults:')
flip_stat = numaric_array('i',0,states_num,0)

for i in range(0,max_flips):
    res = generate_bias_outcome(bias)
    flip_stat[res]+=1

print('\tNumber of Heads',flip_stat[1],'(',round(100*flip_stat[1]/max_flips,2),'%)')
print('\tNumber of Tails',flip_stat[0],'(',round(100*flip_stat[0]/max_flips,2),'%)')
