import numpy as np

# advent of code day 4 2021
# giant squid bingo
# star 6
print("Star 6 ~")


# read and split up file
bingo_base_file = "p4_21_squid_bingo.txt"
with open (bingo_base_file) as bbfile:
    bbfiler = bbfile.read()
    bbstack = bbfiler.split("\n")

# create a class to hold the bingo card, and record the triggered states
class bingocard:
    def __init__(self,matrix):
        self.matrix = matrix
        self.called = np.ones((5,5))

    # checks whether the win condition has been reached
    # if it has, it returns the sum of the uncheck numbers
    def checkwin(self):
        row_x = np.sum(self.called,1).astype(int)
        row_y = np.sum(self.called,0).astype(int)
        condition_checker = np.concatenate((row_x,row_y))
        if 0 in condition_checker:
            uncalled_matrix = self.called*self.matrix.astype(int)
            return sum(np.sum(uncalled_matrix,1))
        else:
            return False

    def checkwin_last(self):
        row_x = np.sum(self.called,1).astype(int)
        row_y = np.sum(self.called,0).astype(int)
        condition_checker = np.concatenate((row_x,row_y))
        if 0 in condition_checker:
            if len(players)>1:
                players.remove(player)

                return False
            else:
                uncalled_matrix = self.called*self.matrix.astype(int)
                return sum(np.sum(uncalled_matrix,1))
        else:
            return False

# format the bingo cards into matrices
ball_pulls = np.array((bbstack[0].split(","))).astype(int)
card_stack = bbstack[2::]
cards = []
for i in range(0,len(card_stack),6):
    cardx = (card_stack[i:i+5])
    for i in range(len(cardx)):
        cardx[i] = cardx[i].split()
    cardx = np.vstack(cardx)
    cards.append(cardx)

# initialise classes to keep track of balls pulled
players = []
for card in cards:
    players.append(bingocard(card))
finished = False
looper = 0

# loop though the ball pulls and play game until the first row is complete
while not finished:
    for pull in ball_pulls:
        for player in players:
            if str(pull) in player.matrix:
                triggered = np.where(player.matrix == str(pull))
                player.called[triggered] = 0
            wincondition = player.checkwin()
            if not wincondition == False:
                final_pull = pull
                break
        if not wincondition == False:
            break
    finished = True

print("sum of remaining values: " + str(int(wincondition)))
print("final score "+ str(int(wincondition*final_pull)))

# star 7
print("Star 7 ~")
# find the score of the board that wins last

# use "checkwin_last" function in class
finished = False
while not finished:
    for pull in ball_pulls:
        for player in players:
            if str(pull) in player.matrix:
                triggered = np.where(player.matrix == str(pull))
                player.called[triggered] = 0
            wincondition2 = player.checkwin_last()
            if not wincondition2 == False:
                final_pull2 = pull
                break
        if not wincondition2 == False:
            break
    finished = True

print(final_pull2)

print("sum of remaining values for the last win: "+ str(int(wincondition2)))
print("final score: "+ str(int(wincondition2*final_pull2)))






