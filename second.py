#loop

i = 1
while(i <=10):
    print(i * '!')
    i = i + 1

j = 1
while(j <=5):
    print('*' * j)
    j = j + 1

secret_num = 5
guess_count = 1
max_count = 3
while guess_count <= max_count:
    guess = int(input("Make a guess :"))
    guess_count = guess_count + 1
    if guess == secret_num:
        print("You win!")
        break
    else:
        print("Try again!")
else:
    print("Sorry, You failed!")
