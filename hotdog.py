print "\tDog \tBun \tKetchup\tMustard\tOnions \tCalories"
dog_cal = 140
bun_cal = 120
mus_cal = 20
ket_cal = 80
onion_cal = 40



count = 1
for dog in [0,1]:
    for bun in [0,1]:
        for ketchup in [0,1]:
            for mustard in [0,1]:
                for onion in [0,1]:
                    total_cal = (dog_cal*dog)+(bun_cal*bun)+(mus_cal*mustard)+(ket_cal*ketchup)+(onion_cal*onion)
                    print "#", count, "\t",
                    print dog, "\t", bun, "\t", ketchup, "\t",
                    print mustard, "\t", onion,
                    print "\t", total_cal
                    count = count + 1
