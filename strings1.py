#%%

# %%
#!/bin/python3

import math
import os
import random
import re
import sys
#%%

a = 'back rack tack'
a = re.sub(" ",'*',a)
print(a)
print(list(a[:6][::-1]))


#%%
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
#

def stringmethod(para, special1, special2, list1, strfind):
    # Write your code here
    combined_pat = list(special1)
    # print(combined_pat)
    word1 = para
    for i in combined_pat:
        word1 = re.sub(re.escape(i),"",word1)
    # word1 = word1.replace('\u0027',"")
    # word1.encode('ascii', 'ignore')
    rword2 = word1[:70][::-1]
    # print(type(rword2))
    # print(list(rword2))
    print(rword2)
    # rword2 = rword2.strip()
    # rword2 = re.sub(" ","",rword2)
    rword2 = rword2.replace(" ","")
    rword2 = list(rword2)
    rword2 = special2.join(rword2)
    print(rword2)
    if all([i in para for i in list1]):
        print(f"Every string in  {list1} were present")
    else:
        print(f"Every string in  {list1} were not present")
    print(word1.split(" ")[:20])
    f_dict = {}
    for i in word1.split(" "):
        if(len(i)>0 and i is not None):
            if(i in f_dict):
                f_dict[i] += 1
            else:
                f_dict[i] = 1
    tmp = [key for key, val in f_dict.items() if val < 3][-20:]
    
    tmp2 = []
    for i in tmp:
        # i = re.sub(r'[^\x00-\x7f]','',i)
        if(len(i)>0 and i is not None):
            tmp2.append(i)

    # tmp2 = [i for i in tmp if i != "" or i != '' or i is not None or i != "'" or len(i) >= 2]
    # print(tmp2)
    # tmp2 = []
    # for i in tmp:
    #     # print(i) 
    #     if(len(i) == 1):
    #         if(ord(i)<128):
    #             i.replace('\u0027','')
    #             i.replace('\u0020','')
    #             tmp2.append(i)
    print(tmp2)


    tmp = re.finditer(strfind, word1)
    for i in tmp:
        z = i.start()
    print(z)
if __name__ == '__main__':
# if __name__ == '__main__':

para = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sem odio, varius nec aliquam nec, tempor commodo ante. Pellentesque sit amet augue vel ante dictum placerat ut ut sapien. Proin maximus eu diam in posuere. Suspendisse in lectus in lectus finibus auctor. Nam sed porttitor arcu. Vestibulum augue odio, posuere quis libero sed, pharetra sollicitudin est. Donec sit amet nunc eu nisi malesuada elementum id ut purus.Nunc sit amet % massa rhoncus, venenatis eros sit amet, ornare augue. Nunc a mi sed est tincidunt facilisis at nec diam. Donec nec ex lorem. Morbi vitae diam tincidunt, dignissim arcu ut, facilisis nisi. Maecenas non felis #ullamcorper, viverra augue id, consequat_nunc. Suspendisse potenti. Proin tempor, sapien ut ornare placerat, sapien mauris luctus sapien, eget aliquam turpis urna at quam. Sed a&eros vel@ ante vestibulum vulputate. Suspendisse vitae vulputate velit. Suspendisse! ligula nisl, semper ut sodales et, ultricies porttitor felis. Nunc ac mattis erat, aliquet pretium risus. Nullam quis congue lacus, et mollis nulla. Nunc laoreet in nisi sit amet facili*sis. Cras rutrum justo ut eros mollis volutpat. Sed quis mi nunc. Nunc sed bibendum nibh, quis bibendum tortor."
special1 = ',_!@*%#$.'
special2 = "|"
"3"
# strfind = "adipiscing"
# "Aliquam"
# "Suspendisse"
strfind ="vulputate"

stringmethod(para,special1,special2,[],strfind)

#%%
z = ['Lorem', 'ipsum', 'dolor', 'consectetur', 'adipiscing', 'elit', 'Aliquam', 'sem', 'odio', 'varius', 'aliquam', 'tempor', 'commodo', 'Pellentesque', 'vel', 'dictum', 'placerat', 'Proin', 'maximus', 'eu', 'posuere', 'lectus', 'finibus', 'auctor', 'Nam', 'porttitor', 'arcu', 'Vestibulum', 'libero', 'pharetra', 'sollicitudin', 'est', 'Donec', 'nunc', 'malesuada', 'elementum', 'id', 'purusNunc', '', 'massa', 'rhoncus', 'venenatis', 'eros', 'ornare', 'a', 'mi', 'tincidunt', 'at', 'ex', 'lorem', 'Morbi', 'vitae', 'dignissim', 'Maecenas', 'non', 'felis', 'ullamcorper', 'viverra', 'consequatnunc', 'potenti', 'mauris', 'luctus', 'eget', 'turpis', 'urna', 'quam', 'Sed', 'a&eros', 'vestibulum', 'vulputate', 'velit', 'ligula', 'nisl', 'semper', 'sodales', 'et']
len(z)



#%%
ido mes mauqilA tile gnicsipida rutetcesnoc tema tis rolod muspi meroL
i,d,o,m,e,s,m,a,u,q,i,l,A,t,i,l,e,g,n,i,c,s,i,p,i,d,a,r,u,t,e,t,c,e,s,n,o,c,t,e,m,a,t,i,s,r,o,l,o,d,m,u,s,p,i,m,e,r,o,L
Every string in  ['adipiscing', 'Aliquam', 'Suspendisse'] were present
['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'Aliquam', 'sem', 'odio', 'varius', 'nec', 'aliquam', 'nec', 'tempor', 'commodo', 'ante', 'Pellentesque', 'sit']
['ultricies', 'ac', 'mattis', 'erat', 'aliquet', 'pretium', 'risus', 'Nullam', 'congue', 'lacus', 'mollis', 'nulla', 'laoreet', 'Cras', 'rutrum', 'justo', 'volutpat', 'bibendum', 'nibh', 'tortor']
851
#%%

my_op1 = "ido mes mauqilA tile gnicsipida rutetcesnoc tema tis rolod muspi meroL"
my_op2 = "i,d,o,m,e,s,m,a,u,q,i,l,A,t,i,l,e,g,n,i,c,s,i,p,i,d,a,r,u,t,e,t,c,e,s,n,o,c,t,e,m,a,t,i,s,r,o,l,o,d,m,u,s,p,i,m,e,r,o,L"
my_op3 = "Every string in ['adipiscing', 'Aliquam', 'Suspendisse'] were present"
my_op4 = "['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'Aliquam', 'sem', 'odio', 'varius', 'nec', 'aliquam', 'nec', 'tempor', 'commodo', 'ante', 'Pellentesque', 'sit']"
my_op5 = "['ultricies', 'ac', 'mattis', 'erat', 'aliquet', 'pretium', 'risus', 'Nullam', 'congue', 'lacus', 'mollis', 'nulla', 'laoreet', 'Cras', 'rutrum', 'justo', 'volutpat', 'bibendum', 'nibh', 'tortor']"
my_op6 = "851"
#%%
s_op1 = "ido mes mauqilA tile gnicsipida rutetcesnoc tema tis rolod muspi meroL"
s_op2 = "i,d,o,m,e,s,m,a,u,q,i,l,A,t,i,l,e,g,n,i,c,s,i,p,i,d,a,r,u,t,e,t,c,e,s,n,o,c,t,e,m,a,t,i,s,r,o,l,o,d,m,u,s,p,i,m,e,r,o,L"
s_op3 = "Every string in  ['adipiscing', 'Aliquam', 'Suspendisse'] were present"
s_op4 = "['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'Aliquam', 'sem', 'odio', 'varius', 'nec', 'aliquam', 'nec', 'tempor', 'commodo', 'ante', 'Pellentesque', 'sit']"
s_op5 = "['ultricies', 'ac', 'mattis', 'erat', 'aliquet', 'pretium', 'risus', 'Nullam', 'congue', 'lacus', 'mollis', 'nulla', 'laoreet', 'Cras', 'rutrum', 'justo', 'volutpat', 'bibendum', 'nibh', 'tortor']"
s_op6 = "851"
#%%
if(my_op3 == s_op3):
    print(True)
else:
    print(False)
# %%
tmp = ['March', '1930', 'later', 'calling', 'for', 'British', 'Quit', 'India', '1942.', 'He', 'was', 'imprisoned', 'many', 'years', 'upon', 'occasions', 'South', 'Africa', 'India.', '']
#%%
''
# %%
