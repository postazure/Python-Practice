addresses = ['123 S. Maple', '8462 W. East Street','8 Maple Lane']

i = int(0)

for lineItem in addresses:
    if 'Maple' in addresses[i]:
        print lineItem + " is item number" + str(i)
    i += 1
        
