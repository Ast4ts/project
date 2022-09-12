n = int(input())
summ = 0
for i in range(n + 1): 
    if n % 2 == 0: 
        summ += (i + 1)
    else:
        summ -= (i + 1)
print(summ)