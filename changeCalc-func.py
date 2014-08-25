def coinCounter(q,d,n,p):
    total=(q*.25)+(d*.10)+(n*.05)+(p*.01)
    return total

quarters = int(raw_input("Number of Quarters: "))
dimes = int(raw_input("Number of Dimes: "))
nickels = int(raw_input("Number of Nickels: "))
pennies = int(raw_input("Number of Pennies: "))

totalCoin = coinCounter(quarters,dimes,nickels,pennies)

print "Total Amount: ", totalCoin
