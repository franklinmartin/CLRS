## Problems

### 1-1 Comparison of running times

> For each function $f(n)$ and time $t$ in the following table, determine the largest size n of a problem that can be solved in time $t$ , assuming that the algorithm to solve the problem takes $f(n)$ microseconds.

|            |  1 second  |  1 minute  |   1 hour   |   1 day    |  1 month   |   1 year   | 1 century  |
|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
|  $lgn$   |$2^{10^6}$|$2^{6 \times 10^{6}}$|$2^{3.6 \times 10^{9}}$|$2^{8.64 \times 10^{10}}$|$2^{2.59 \times 10^{12}}$|$2^{3.15 \times 10^{13}}$|$2^{3.15 \times 10^{15}}$|
|$\sqrt{n}$|$10^{12}$ |$3.6 \times 10 ^{15}$|$1.3 \times 10^{19}$|$7.46 \times 10^{21}$|$6.72 \times 10^{24}$|$9.95 \times 10^{26}$|$9.95 \times 10^{30}$|
|   $n$    |$10^6$|$6 \times 10 ^{7}$|$3.6 \times 10 ^{9}$|$8.64 \times 10 ^{10}$|$2.59 \times 10 ^{12}$|$3.15 \times 10 ^{13}$|$3.15 \times 10 ^{15}$|
|  $nlgn$  |$6.24 \times 10 ^{4}$|$2.8 \times 10 ^{6}$|$1.33 \times 10 ^{8}$|$2.76 \times 10 ^{9}$|$7.19 \times 10 ^{10}$|$7.98 \times 10 ^{11}$|$6.86 \times 10 ^{13}$|
|  $n^2$   |$1000$|$7745$|$60000$|$293938$|$1609968$|$5615692$|$56156922$|
|  $n^3$   |$100$|$391$|$1532$|$4420$|$13736$|$31593$|$146645$|
|  $2^n$   |$19$|$25$|$31$|$36$|$41$|$44$|$51$|
|   $n!$   |$9$|$11$|$12$|$13$|$15$|$16$|$17$|

```python
import math

second = 1
minute = 60
hour = 3600
day = int(24*hour)
month = int(30.4375*day)
year = int(12*month)
century = int(100*year)

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

bs = [1e40, 1e40, 1e40, 1e20, 1e20, 1000, 100]
TOL = 1
f_result = []
for i in range(len(functions)):
    result = []
    for t in range(len(times)):
        a = 1
        b = bs[i]
        n = 1
        # terminates in log (b-a / TOL) ~ log(b)/log(2) ~ 133 steps, TOL = 1
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
#print(f_result)

```
