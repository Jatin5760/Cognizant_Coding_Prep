# Contiginuous
# Simlar types of element or can be heterogenous also


# How we can use arrays?

# 1) We can use python array module
# 2) We can use numpy python arrays

import array
vals = array.array('i', [1,2,3,4,5,6])


'''This is enhanced for loop'''
# for val in vals:
#     print(val)


'''This is traditional for loop'''
for i in range(0, len(vals)):
    print(vals[i], end=" ")
    

'''Type codes array'''
print('\n')
print(vals.typecode)


'''Reversing an array'''
vals.reverse()
print('\n')
for x in vals:
    print(x, end=" ")