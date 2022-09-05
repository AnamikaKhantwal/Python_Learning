#basic
Weight = float(input("Weight: "))
meas = input("(k)g or (L)bs: ")

if meas.upper()=="K":
    newweight = Weight * 2.20462
    print("Weight is " + str(newweight))
elif meas.upper()=="L":
    newweight = Weight * 0.453592
    print("Weight is " + str(newweight))
print('Done')
msg = f'{Weight} [{Weight}] is this' #formatted string
print(msg)
