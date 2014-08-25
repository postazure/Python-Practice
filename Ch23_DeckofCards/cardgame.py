import random
from cards import Card

deck = []
suit =''
rank = 0
for suit_id in range(1,5):
    for rank_id in range(1,14):
        new_card = Card(suit, rank)
        if new_card.rank == 8:
            new_card.value = 50        
        deck.append(Card(suit_id,rank_id))

hand = []
for cards in range(0,5):
    a = random.choice(deck)
    hand.append(a)
    deck.remove(a)

print
for card in hand:
    print card.short_name, '=', card.long_name, " Value:", card.value

def player_turn():
    global deck, p_hand, blocked, up_card, active_suit

    
    print"\nYour hand:",
    for card in p_hand:
        print card.short_name,
        print " Up card: ", up_card.short_name
    if up_card.rank == '8':
        print " Suit is", active_suit

    print "What would you like to do? ",
    response = raw_input("type a card to play or 'Draw' to take a card: ")
    valid_play = False
    is_eight = False

    while not valid_play:
        selected_card = None
        while selected_card == None:
            if response.lower() == 'draw':
                valid_play = True
                if len(deck) > 0:
                    card = random.choice(deck)
                    p_hand.append(card)
                    deck.remove(card)
                    print "You drew", card.short_name
                else:
                    print "There are no cards left in the deck"
                    blocked += 1
                return
            else:
                for card in p_hand:
                    if response.upper() == card.short_name:
                        selected_card = card
                if selected_card == None:
                    response = raw_input("You don't have that card. Try again:")
                if selected_card.rank == '8':
                    valid_play = True
                    is_eight = True
                elif selected_card.suit == active_suit:
                    valid_play = True
                elif selected_card.rank == up_card.rank:
                    valid_play = True

                if not valid_play:
                    response = raw_input("That's not a legal play. Try again: ")

            p_hand.remove(selected_card)
            up_card = selected_card
            active_suit = up_card.suit
            print "You played", selected_card.short_name
            if slected_card.rank == '8':
                get_new_suit()
            
def get_new_suit():
    global active_suit
    got_suit = False
    while not got_suit:
        suit = raw_input("Pick a suit: ")
        if suit.lower() == 'd':
            active_suit = "Diamonds"
            got_suit = True
        elif suit.lower() == 's':
            active_suit = 'Spades'
            got_suit = True
        elif suit.lower() == 'h':
            active_suit = 'Hearts'
            got_suit = True
        elif suit.lower() == 'c':
            active_suit = 'Clubs'
            got_suit = True
        else:
            print "Not a vaild suit. Try again. ",
    print "You picked", active_suit

def computer_turn():
    global c_hand, deck, up_card, active_suit, blocked
    options = []
    for card in c_hand:
        if card.rank =='8':
            c_hand.remove(card)
            up_card = card
            print " Computer played ", card.short_name
            #suit totals: d,h,s,c
            suit_total = [0,0,0,0]
            for suit in range(1,5):
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit-1] += 1
            long_suit = 0
            for i in range(4):
                if suit_totals[i] > long_suit:
                    long_suit = 1
            if long_suit == 0: active_suit = "Diamonds"
            if long_suit == 1: active_suit = "Hearts"
            if long_suit == 2: active_suit = "Spades"
            if long_suit == 3: active_suit = "Clubs"
            print " Computer changed suit to ", active_suit
            return
        else:
            if card.suit == active_suit:
                options.append(card)
            elif card.rank == up_card.rank:
                options.append(card)
    if len(options) > 0:
        best_play = options[0]
        for card in options:
            if card.value > best_play.value:
                best_play = card

        c_hand.remove(best_play)
        up_card = best_play
        active_suit = up_card.suit
        print " Computer played ", best_play.short_name

    else:
        if len(deck) > 0:
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print " Computer drew a card"
        else:
            print " Computer is blocked"
            blocked += 1
    print " Computer has %i cards left" % (len(c_hand))
    
            


done = False
p_total = c_total =0
while not done:
    blocked = 0
    game_done = False
    init_cards()    
    while not game_done:
        
        player_turn()
        if len(p_hand) == 0:
            game.done = True
            print
            print 'You Win!'
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            print "You got %i points for computer's hand" % p_points
            
        if not game_done:
            computer_turn()
        if leg(c_hand) == 0:
            game_done = True
            print
            print "Computer Win :("
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print "Computer got %i points for your hand" % c_points
                        


        if blocked >= 2:
            game_done =True
            print "Both players blocked. Game Over"
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            print "You got %i points for computer's hand" % p_points
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print "Computer got %i points for your hand" % c_points

            
    play_again = raw_input("Play again(Y/N)? ")
    if play_again.lower().startswith('y'):
        done = False
        print"\nSo far, you have %i points" % p_total
        print "and the Computer has %i points.\n" %c_total
    else:
        done = True
print "\nFinal Score:"
print "You %i\tComputer: %i" %(p_total,c_total)
