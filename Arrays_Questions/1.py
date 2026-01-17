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
    

'''Inserting element in array'''
vals.insert(1, 50)
vals.append(100)

# Overide the element
# vals[2] = 200

print('\n')
for x in vals:
    print(x, end=" ")
    
    

'''Copy an array'''
print('\n')
copyArray = array.array(vals.typecode, (x**3 for x in vals))
for i in range(0, len(copyArray)):
    print(copyArray[i], end=" ")
    
    
'''Delete the element'''
copyArray.pop(3)
print('\n')
for i in range(0, len(copyArray)):
    print(copyArray[i], end=" ")
    
# copyArray.remove(216) Directly removing with the help of value of element


