from color_data import days_colors  # Import the dictionary
from collections import Counter
import statistics

# 4.      BONUS Get the variance of the colors
# Combine all colors into one list
all_colors = []
for day in days_colors.values():
    all_colors.extend(day)

# Calculate frequency of each color
color_freq = Counter(all_colors)
frequencies = list(color_freq.values())

# Calculate sample variance
variance = statistics.variance(frequencies)

# Print results
print("Color frequencies:", dict(color_freq))
print(f"Variance of the color frequencies: {variance:.2f}")