from scipy.stats import binom

n = 10
p = 0.5

probability = binom.pmf(2, n, p) + binom.pmf(3, n, p) + binom.pmf(4, n, p)

print(probability)