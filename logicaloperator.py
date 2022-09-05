name = input("Enter you name ")
name_length = len(name)

if name_length < 3:
    print("Error : Name must be atleast 3 characters long")
elif name_length > 50:
    print("Error : Name can be of 50 characters only")
else:
    print("Name looks good!")
