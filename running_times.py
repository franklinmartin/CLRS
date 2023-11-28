import math

second = 1
minute = 60
hour = 3600
day = int(24*hour)
month = int(30.4375*day)
year = int(12*month)
century = int(100*year)
#print(second)
#print(minute)
#print(hour)
#print(day)
#print(month)
#print(year)
#print(century)

times = [second, minute, hour, day, month, year, century]
for i in range(0, len(times)):
    times[i] = times[i] * (10 ** 6)
#print(times)

lambda n : math.log2(n)

#log(n) = t
#n = 2^t
functions = [lambda n : math.sqrt(n),
             lambda n : n,
             lambda n : n * math.log2(n),
             lambda n : n ** 2,
             lambda n : n ** 3,
             lambda n : math.exp2(n),
             lambda n : math.factorial(n)]

bs = [1e40, 1e40, 1e40, 1e40, 1e40, 100, 100]
#40 20 20 10 10 100 100
TOL = 1
f_result = []
for i in range(len(functions)):
    result = []
    for t in range(len(times)):
        a = 1
        b = bs[i]
        n = 1
        # terminates in log (b-a / TOL) ~ log(b)/log(2) ~ 133 steps, TOL = 1
        # 4618 total steps
        while True:
            c = (a + b) // 2
            if functions[i](c) - times[t] == 0 or (b - a) // 2 < TOL:
                result.append(c)
                break
            n += 1
            if (functions[i](c) - times[t] < 0 and functions[i](a) - times[t] < 0) or (
                    functions[i](c) - times[t] > 0 and functions[i](a) - times[t] > 0):
                a = c
            else:
                b = c
    if i < 3:
        print(' '.join(map(lambda s: '{:.3e}'.format(s), result)))
    else:
        print(' '.join(map(lambda s: str(int(math.floor(s))), result)))
    f_result += result
print(f_result)