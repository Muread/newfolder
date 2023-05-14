import random
import statistics

N = 1000000
A = [random.randint(0, 1000) for i in range(N)]
B = [a + 100 for a in A]
mean_B = statistics.mean(B)

print(mean_B)