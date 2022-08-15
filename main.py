# advent of code day 1 2021
# ~ basic puzzle
# how many measurements are larger than the previous measurement

# read file
radar_value_file = "P1_21_radar_vals.txt"
with open(radar_value_file) as radar_vals_f:
    radar_vals = radar_vals_f.read()
    radar_vals = radar_vals.split()

# count values larger than previous index
increase_counter = 0
radar_vals_l = len(radar_vals)
for i in range(radar_vals_l):
    radar_val = float(radar_vals[i])
    if i>0:
        if radar_val>float(radar_vals[i-1]):
            increase_counter +=1

# Print the output
print(str(increase_counter) + " values were larger than their preceding value.")