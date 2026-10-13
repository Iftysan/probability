
from scipy.stats import poisson

expected_rainy_days = 10

probability_12_or_more = poisson.sf(11, mu=expected_rainy_days)

probability_between_12_and_18 = poisson.cdf(18, mu=expected_rainy_days) - poisson.cdf(11, mu=expected_rainy_days)

print("Probability of 12 or more rainy days:", probability_12_or_more)
print("Probability of between 12 and 18 rainy days:", probability_between_12_and_18)
