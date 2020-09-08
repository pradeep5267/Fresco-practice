#%%
#!/bin/python3

import math
import os
import random
import re
import sys


import datetime
#
# Complete the 'dateandtime' function below.
#
# The function accepts INTEGER val as parameter.
# The return type must be LIST.
#


def dateandtime(val,tup):
    # Write your code here
    ans_list = []
    if(val == 1):
        # a = datetime.datetime._build_struct_time(tup[0],tup[1],tup[2],None,None,None,None)
        tmp = datetime.date(tup[0],tup[1],tup[2])
        ans_list.append(tmp)
        tmp = str(tmp.strftime('%d/%m/%Y'))
        ans_list.append(tmp)

    elif(val == 2):
        # tmp = datetime.datetime.fromordinal(tup[0])
        print(tup[0])
        tmp = datetime.datetime.fromtimestamp(tup[0]).date()
        # datetime.datetime.strptime(tmp, '%Y-%m-%d')
        ans_list.append(tmp)
        print(ans_list)

    elif(val == 3):
        tmp = datetime.time(tup[0],tup[1],tup[2])
        # tmp2 = datetime.datetime.strptime(str(tmp.hour), "%H")
        tmp2 = tmp.strftime("%I")
        ans_list.append(tmp)
        ans_list.append(tmp2)
        # print(ans_list)
    
    elif(val == 4):
        tmp = datetime.date(tup[0],tup[1],tup[2])
        # print(tmp.day,tmp.month)
        ans_list.append(datetime.datetime.strftime(tmp,"%A"))
        ans_list.append(datetime.datetime.strftime(tmp,"%B"))
        ans_list.append(datetime.datetime.strftime(tmp,"%j"))
        # print(ans_list)
    
    elif(val == 5):
        # tmp = datetime.date(tup[0],tup[1],tup[2],tup[3],tup[4],tup[5])
        # print(tmp)
        d = datetime.date(tup[0],tup[1],tup[2])
        t = datetime.time(tup[3],tup[4],tup[5])
        tmp = datetime.datetime.combine(d, t)
        ans_list.append(tmp)
        # print(ans_list)


# if __name__ == '__main__':
#     val = int(input().strip())
    
#     if val ==1 or val==4 or val ==3:
#         qw1_count=3
#     if val==2:
#         qw1_count=1
#     if val ==5:
#         qw1_count=6
#     qw1 = []

#     for _ in range(qw1_count):
#         qw1_item = int(input().strip())
#         qw1.append(qw1_item)
        
#     tup=tuple(qw1)

val=2
tup=(1258094605,)
ans = dateandtime(val,tup)

# val=3
# tup = ( 22, 34, 56)
# ans = dateandtime(val,tup)

# val=4
# tup = (2022, 9, 11)
# ans = dateandtime(val,tup)

# val=5
# tup = ( 2017, 11, 28, 23, 55, 59)
# ans = dateandtime(val,tup)

print(ans)
# %%
'''
STDIN      Function
-----      --------
3           → val=3
22          → tup = ( 22, 34, 56)
34
56

[datetime.time(22, 34, 56), '10']
#%%
STDIN      Function
-----      --------
4           → val=4
2020        → tup = ( 2022, 9, 11)
9
11

['Friday', 'September', '255']
#%%
STDIN      Function
-----      --------
5           → val=5
2017        → tup = ( 2017, 11, 28, 23, 55, 59)
11
28
23
55
59

[datetime.datetime(2017, 11, 28, 23, 55, 59)]
'''