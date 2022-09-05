#list - defined using []

names = ["A", "B", "C", "D"]
names[-1] = "Z"
print(names[0:3])
names.append("E")
print(names)
names.insert(3, "F")
print(names)
#names.clear()
print(names)
print("A" in names)
print(len(names))

numbers = [3, 5, 7, 8]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#2D lists

