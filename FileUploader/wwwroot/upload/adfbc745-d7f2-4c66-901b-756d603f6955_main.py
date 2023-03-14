numbers = [2,4,6,8,1,3]

for number in numbers:
    if number % 2 == 1:
        print(f"There is Odd number : {number}" )
        break
else:
    print("There is no odd number")
