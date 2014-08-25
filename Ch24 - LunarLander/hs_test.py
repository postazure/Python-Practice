def disp_high_score():
    high_scores = []
    
    hs_file = open("high_score.txt",'r')    
    high_scores = hs_file.readlines()
    high_scores = map(int, high_scores)
    hs_file.close()

    high_scores.append(int(fuel))
    high_scores.sort()
    high_scores.reverse()
        
    del high_scores[3]
    hs_file = open("high_score.txt",'w')
    for scores in high_scores:
        hs_file.write(str(scores) + '\n')
    hs_file.close

fuel = raw_input("New score?")
disp_high_score()


