import random

totals = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(10000):
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    dice_total = dice_1 + dice_2
    totals[dice_total] += 1

for i in range(2,13):
    print "total", i, "came up", totals[i], "times"
    
