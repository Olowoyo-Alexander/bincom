from color_data import days_colors
from collections import Counter

# 2.      Which color is mostly worn throughout the week?
# Combine all colors into one list
all_colors = []
for day in days_colors.values():
    all_colors.extend(day)

# Calculate frequency of each color
color_freq = Counter(all_colors)

# Find the color with the highest frequency
most_common_color, frequency = color_freq.most_common(1)[0]  # Returns a list of (color, count) tuples, take the first

# Print the result
print(f"The most worn color throughout the week is '{most_common_color}' with {frequency} occurrences.")