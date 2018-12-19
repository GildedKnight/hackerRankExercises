#basic set operations on both numerical and alphabetical sets
#Intersection: Common elements of set a and b;
#Union: All elements of set a and b;
#Difference: Elements only present in set a, if a-b, Elements only present in set b, if b-a;
#Symmetric Difference: Unique elements in set a and b;

a = {2,4,6,8,10};
b = {1,2,3,4,5,6};
c = {'apple','banana','orange','litchi','berries'};
d ={'mango','apple','grapes','banana','melon','orange'};

print('Union of numerical set:', a|b)
print('\n')
print('Union of string set:', c|d)
print('\n')
print('Intersection numerical set: ', a&b)
print('\n')
print('Intersection string set: ', c&d)
print('\n')
print('Difference numerical set: ', a-b)
print('\n')
print('Difference string set: ', c-d)
print('\n')
print('Symmetric Difference numerical set: ', a^b)
print('\n')
print('Symmetric Difference string set: ', c^d)
