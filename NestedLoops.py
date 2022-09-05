for x in range(5):
    for y in range(5):
        print(f"({x}, {y})")


numbers = [5, 2, 5, 2, 2]
for item in numbers:
    print(item * "X")

#numbers = [5, 2, 5, 2, 2]
#for item in numbers:
  #  for y in numbers:
   #     print(f"{y * 'X'}")

numbers = [2, 2, 2, 2, 5]
for item in numbers:
    output = ''
    for count in range(item):
        output += 'X'
    print(output)