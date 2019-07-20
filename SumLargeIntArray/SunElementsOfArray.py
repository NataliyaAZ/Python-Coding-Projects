x = [234567,65536345656,44444444444444444444444444444444444444444444444444444444444444444444444444444444,45]
i = 0
sum = 0
while i < len(x):
    sum = sum +x[i]
    i +=1 
print(sum,type(sum))

#Integers in Python 3 are of unlimited size. Python 2 has two integer types - int and long. 
#There is no 'long integer' in Python 3 anymore.