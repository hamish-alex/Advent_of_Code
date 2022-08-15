# advent of code day 3 2021
# ~ basic puzzle
# use binary input to produce a diagnostic reports
import numpy as np
import pandas as pd


# star 5
print("Star 5 ~")
# get gamma rate and epsilon rate
# get power consumption by multiplying the two
# gamma rate is found by getting the most common bit in each position
# epsilon rate is the least common bit

# convert data to matrix
diag_file = "p3_21diagnosticsbinary.txt"
primary_check = True
bit_stack = []
with open(diag_file) as diagnostics:
    for line in diagnostics.readlines():
        linerow = []
        linerow[:0] = line
        linerow.pop()
        listrow = np.array(linerow).astype(float)
        bit_stack.append(listrow)
bit_matrix = np.vstack(bit_stack)
bm_rows, bm_cols = bit_matrix.shape
# average all rows
ave_matrix = np.sum(bit_matrix, axis = 0)/bm_rows

# convert values larger than 0.5 to 1's, less to 0's
gamma_binary = (ave_matrix>=0.5).astype(int)
epsilon_binary = (ave_matrix<0.5).astype(int)
print("gamma binary: "+str(gamma_binary))
print("epsilon binary: "+ str(epsilon_binary))

# convert binary to base 10
gamma_val = 0
for i in range(len(gamma_binary)):
    gamma_val += gamma_binary[::-1][i]*2**i
print("gamma value: "+ str(gamma_val))
epsilon_val = 0
for i in range(len(epsilon_binary)):
    epsilon_val += epsilon_binary[::-1][i]*(2**i)
print("gamma value: "+ str(epsilon_val))

power_consumption = epsilon_val*gamma_val
print("power consumption: "+ str(power_consumption)+"\n")


# star 6
print("Star 6 ~")

# extract "oxygen generator rating" and "CO2 scrubber rating"
# iterate over columns and filter rows with either the most or least common bit
#   stop when only one row remains
def common_columns(matrixinp,most_common = True):
    remaining_vector = pd.DataFrame(matrixinp)
    ncols = remaining_vector.shape[1]
    for col_n in range(ncols):
        nrows = remaining_vector.shape[0]
        if nrows <=1:
            return list(remaining_vector.iloc[0])
        col_max = sum(remaining_vector.iloc[:,col_n])/nrows
        if most_common:
            if col_max>=0.5:
                col_val_select = 1
            else:
                col_val_select = 0
        elif not most_common:
            if col_max>=0.5:
                col_val_select = 0
            else:
                col_val_select = 1
        remaining_vector = remaining_vector[remaining_vector.iloc[:,col_n]==col_val_select]
    return list(remaining_vector.iloc[0])

# Find the oxygen generator rating (common bit case)
oxygen_rating_bits = common_columns(bit_matrix)
oxygen_rating = 0
# convert to base 10
for i in range(len(oxygen_rating_bits)):
    oxygen_rating += oxygen_rating_bits[::-1][i]*2**i
print("oxygen_rating: "+ str(int(oxygen_rating)))

# Find the oxygen generator rating (uncommon bit case)
co2_rating_bits = common_columns(bit_matrix,False)
co2_rating = 0
# convert to base 10
for i in range(len(co2_rating_bits)):
    co2_rating += co2_rating_bits[::-1][i]*(2**i)
print("co2_rating: "+ str(int(co2_rating)))

# find the "life support rating" by multiplying the two
life_support_rating = co2_rating*oxygen_rating
print("life support rating: " + str(int(life_support_rating)))