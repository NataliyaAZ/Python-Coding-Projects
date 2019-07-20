x = [5,10,45,-456,3456,-67,9867]
i = 0
sum = 0
while i < len(x):
    if x[i]%2 == 1:
        sum = sum + x[i]
    i += 1
print(sum)
