from color_data import days_colors
# 1.      Which color of shirt is the mean color?

all_colors = []
for day in days_colors:
    all_colors.extend(days_colors[day])

color_count = {}
for color in all_colors:
    color_count[color]=color_count.get(color, 0) + 1

mean_color = max(color_count,key=color_count.get)
frequency= color_count[mean_color]

print("color frequency:", color_count)
print(f'the "mean" color (most frequency) is: { mean_color} with {frequency} occurrence')
