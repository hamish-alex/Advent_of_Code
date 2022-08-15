# advent of code day 2 2021
# ~ basic puzzle
# change the coordinates of the submarine

# star 3
print("Star 3 ~")
# create a class to keep track of submarine positions
class submarine:
    def __init__(self):
        self.xpos = 0  # forward/ back
        self.ypos = 0  # left/right
        self.zpos = 0
        self.aim = 0
second_sub = submarine()

# break up the input into instructions
instruction_filename = "P2_21_sub_instructions.txt"
with open(instruction_filename) as instructions:
    instructions = (instructions).read()
    instruction_list = instructions.split()

# apply instructions and reposition submarine
for i in range(0,len(instruction_list),2):
    instruction_type = instruction_list[i]
    movement_value = int(instruction_list[i+1])
    if instruction_type == "forward":
        second_sub.xpos += movement_value
    if instruction_type =="up":
        second_sub.zpos += movement_value
    if instruction_type =="down":
        second_sub.zpos -= movement_value

print("sub height: " + str(second_sub.zpos) + " sub distance: " + str(second_sub.xpos))
print("Star 3 solution: " + str(second_sub.zpos * second_sub.xpos)+"\n")


# star 4
print("Star 4 ~")
# add new "aim" functionality for the moves

# added aim to the class
# initialise a new submarine with the introduction of the "aim" attribute
# use this aim attribute to change depth
second_sub = submarine()
for i in range(0,len(instruction_list),2):
    instruction_type = instruction_list[i]
    movement_value = int(instruction_list[i+1])
    if instruction_type == "forward":
        second_sub.xpos += movement_value
        second_sub.zpos += second_sub.aim*movement_value
    if instruction_type =="up":
        second_sub.aim -= movement_value
    if instruction_type =="down":
        second_sub.aim += movement_value
print("final depth: "+ str(second_sub.zpos)+ " final horizonal position: "+ str(second_sub.xpos))
print("star 4 solution: "+ str(second_sub.zpos*second_sub.xpos)+"\n")

