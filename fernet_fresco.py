#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'encrdecr' function below.
#
# The function is expected to return a LIST.
# The function accepts following parameters:
#  1. STRING keyval
#  2. STRING textencr
#  3. Byte-code textdecr
#
from cryptography.fernet import Fernet
def encrdecr(keyval, textencr, textdecr):
    # Write your code here
    ans_list = []
    cipher_suite = Fernet(keyval)
    enc_text = Fernet.encrypt(cipher_suite,textencr)
    dec_bytes = Fernet.decrypt(cipher_suite,textdecr).decode("utf-8")
    ans_list.append(enc_text)
    ans_list.append(dec_bytes)
    return ans_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
    file = open('key.key', 'rb')
    key = file.read()  # The key will be type bytes
    file.close()
    
    keyval = key

    textencr = str(input()).encode()

    textdecr = str(input()).encode()


    result = encrdecr(keyval, textencr, textdecr)
    bk=[]
    f = Fernet(key)
    val = f.decrypt(result[0])
    bk.append(val.decode())
    bk.append(result[1])

    fptr.write(str(bk) + '\n')

    fptr.close()


'''
STDIN                                              Function
-----                                              --------
the union government created by the constitution of India       →  textencr
as the legislative, executive and judicial authority of the
 union of twenty eight states and nine union territories of
 a constitutionally democratic republic

gAAAAABe2NXpWXfN35D4SGJKLvDuI370wRgIHXoNvV6gaVuJjuXEasIVRqsK    →  textdecr
wAu4-DluBuhufFF5bewvqpEBxIbmrh1CfEiOuyPpKvS8sqDi7-p6IjflGqA3h
9Liaze1x2x_tL4mI3KB

['the union government created by the constitution of India as the legislative, executive and judicial authority of the union of twenty eight states and nine union territories of a constitutionally democratic republic', 'TCS is one of the largest job creators in India']
'''