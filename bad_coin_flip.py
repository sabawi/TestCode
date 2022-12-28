# Developer : Al Sabawi

import sys
import numpy as np
import time
import array as arr

def numaric_array(atype,index_start,index_end,init_value):
    return arr.array(atype,(init_value for i in range(index_start,index_end)))

def generate_random_number():
    return np.random.random()

def generate_bias_outcome(b=0.5):
    if generate_random_number() < b:
        return 1
    else:
        return 0
def flip_a_coin(bias):
    return(generate_bias_outcome(bias))

def flip_a_coin_many_times(bias,flips):
    states_num = 2 # 2 states, Head and Tail

    flip_stat = numaric_array('i',0,states_num,0)
    for i in range(0,flips):
        res = flip_a_coin(bias)
        flip_stat[res]+=1
    return(flip_stat)

def print_input_err(inparm):
    print('Argument',inparm, 'is not a float data type. Try again.')

def get_arguments():   
    if __name__ == "__main__":
        if len(sys.argv) > 1:
            try:
                arg_in = float(sys.argv[1])
            except ValueError:
                print_input_err(sys.argv[1])
                quit()

            bias = float(sys.argv[1])
            if(bias>1.0):
                print_input_err(sys.argv[1])
                quit()

            print('Bias = ',bias*100,"% for Head")
        else:
            print ( '*** Usage:',sys.argv[0], '<bias factor as fraction between 0.0 to 1.0>\n')
            quit()
    return(bias)

def run():
    max_flips = 100000
    np.random.seed(int(time.time()))

    print('Testing a coin flip', max_flips,'times. \nResults:')

    bias = get_arguments()

    flip_stat = flip_a_coin_many_times(bias,max_flips)

    print('\tNumber of Heads',flip_stat[1],'(',round(100*flip_stat[1]/max_flips,2),'%)')
    print('\tNumber of Tails',flip_stat[0],'(',round(100*flip_stat[0]/max_flips,2),'%)')

run()