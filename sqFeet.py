widthSize = float(raw_input("Width Size?"))
lengthSize = float(raw_input("Length Size?"))

totalSize = widthSize*lengthSize

carpetCost = float(raw_input("Cost per sqft.?"))


print "You require ", totalSize , "feet of carpet."
print "However, it is advisable to add 15% to account for waste, so ", totalSize*1.15 , "feet."
print "Total cost is $", totalSize*carpetCost
