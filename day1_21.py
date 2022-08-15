# advent of code day 1 2021
# ~ basic puzzle
# how many measurements are larger than the previous measurement
import numpy as np

# star one
print("Star 1 ~")

# read file
radar_value_file = "P1_21_radar_vals.txt"
with open(radar_value_file) as radar_vals_f:
    radar_vals = radar_vals_f.read()
    radar_vals = np.array(radar_vals.split())
    radar_vals = radar_vals.astype(float)

# count values larger than previous index
def count_larger(value_list):
    increase_counter = 0
    radar_vals_l = len(value_list)
    for i in range(radar_vals_l):
        radar_val = float(value_list[i])
        if i>0:
            if radar_val>float(value_list[i-1]):
                increase_counter +=1
    return(increase_counter)

# Print the output
value_count = count_larger(radar_vals)
print("Star one solution: "+ str(value_count) + " values were larger than their preceding value.\n")


# star two
print("Star 2 ~")
# count the number of three value sets that are larger than the previous set

# sum up data into windows of length three
radar_windows = np.ones(len(radar_vals)-2)
radar_windows_l = len(radar_windows)
for i in range(radar_windows_l):
    radar_windows[i] = sum(radar_vals[i:i+3])

# count increasing values
window_value_count = count_larger(radar_windows)
print("Star two solution: " + str(window_value_count) + " values were larger than their preceding value.")






