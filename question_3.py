from color_data import days_colors

# 3.Which color is the median?
all_colors = []
for day in days_colors:
    all_colors.extend(days_colors[day])

n = len(all_colors)
all_colors_sorted = sorted(all_colors)
median_position = (n+1) // 2 
median_color = all_colors_sorted[median_position-1]

print(f'Total numbers of colors: {n}')
print(f'sorted list of colors: {all_colors_sorted}')
print(f' median position: {median_position}')
print(f'The median color is: {median_color}')