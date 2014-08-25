#Adds up value of coins for a total

qtyQ = int(raw_input("How many Quarters?"))
qtyD = int(raw_input("How many Dimes?"))
qtyN = int(raw_input("How many Nickels?"))
qtyP = int(raw_input("How many Pennies?"))

totalValue = qtyQ*.25 + qtyD*.10 + qtyN*.05 + qtyP*.01

print "You have $"+ str(totalValue) + "."
