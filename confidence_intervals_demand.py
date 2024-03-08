# Importing scipy.stats for necessary calculations - provides statistical functions
import scipy.stats as stats

# Daily demand
mean = 480
standard_deviation = 200

# Sample size
sample_size = 360

# Confidence levels
confidence_90 = 0.90
confidence_95 = 0.95
confidence_999 = 0.999

# Calculate the critical z-values for each confidence level - number of standard deviations from the mean
z_90 = stats.norm.ppf(1 - (1 - confidence_90) / 2)
z_95 = stats.norm.ppf(1 - (1 - confidence_95) / 2)
z_999 = stats.norm.ppf(1 - (1 - confidence_999) / 2)

# Calculate confidence intervals
ci_90 = (mean - z_90 * (standard_deviation / (sample_size ** 0.5)), mean + z_90 * (standard_deviation / (sample_size ** 0.5)))
ci_95 = (mean - z_95 * (standard_deviation / (sample_size ** 0.5)), mean + z_95 * (standard_deviation / (sample_size ** 0.5)))
ci_999 = (mean - z_999 * (standard_deviation / (sample_size ** 0.5)), mean + z_999 * (standard_deviation / (sample_size ** 0.5)))

# Printing the results
print("The Confidence Interval for 90% is:", ci_90)
print("The Confidence Interval for 95% is:", ci_95)
print("The Confidence Interval for 99.9% is:", ci_999)
