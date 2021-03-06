# Could not remember if I should use randint or randrange so checked that
# randint would randomly generate all four of the numbers 1, 2, 3, 4

import random

NUM_TRIALS = 100
winnings = 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS):
    # prize = ""
    round_winnings = 0

    for things in range(0, 3):

        # randint finds numbers between given endpoints, including both endpoints
        prize_num = random.randint(1,100)
        # prize += " "
        if 0 < prize_num <= 5:
            round_winnings += 5
        elif 5 < prize_num <= 25:
            round_winnings += 2
        elif 25 < prize_num <= 65:
            round_winnings += 1
        '''else:
            prize += "lead"'''

    # print("You own {} which is worth {}".format(prize, round_winnings))
    winnings += round_winnings

print("Paid In: ${}".format(cost))
print("Pay out: ${}".format(winnings))

if winnings > cost:
    print("You came out ${} ahead".format(winnings - cost))
else:
    print("Sorry, you lost ${}".format(cost-winnings))