sample = input("Introduce numbers separated by ,: ")
sample = sample.split(',')
n = len(sample)
for x in range(n):
    sample[x] = float(sample[x])
sample = tuple(sample)
sum_val = 0
sumsq = 0
for x in sample:
    sum_val += x
    sumsq += x**2
avg = sum_val / n
stdev = (sumsq / n - avg**2)**(1/2)
print('The average is', avg, ', his deviation is of ', stdev)   