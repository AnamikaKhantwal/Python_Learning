#for loop
import math
nums = [1, 2, 3, 4, 5]
print(nums)

for item in nums:
    print(item)

i =0
while i < len(nums):
    print(nums[i])
    i = i + 1

#range funtion

numbers = range(5, 20, 3)
print(numbers)
for item in numbers:
    print(item)

sum = 0
prices = [10, 20, 30]
for item in prices:
    sum = sum + item
print(sum)