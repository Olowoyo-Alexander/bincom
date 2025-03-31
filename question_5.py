
from color_data import days_colors
# 5.      BONUS if a colour is chosen at random, what is the probability that the color is red?

total_colors = 0
red_count = 0

for day, colors in days_colors.items():
    total_colors += len(colors)  # Add the number of colors for this day
    red_count += colors.count("RED")  # Count "RED" occurrences for this day

# Calculate probability
probability_red = red_count / total_colors

# Output results
print(f"Total colors: {total_colors}")
print(f"Number of RED: {red_count}")
print(f"Probability of RED: {probability_red:.4f} (or {red_count}/{total_colors})")

