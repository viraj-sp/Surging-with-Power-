def powerof4(number):
    if number <= 0:
        return False
   
    if number & (number - 1) != 0:
        return False
   
    count = 0
    while number > 1:
        number >>= 1
        count += 1
    #
    return count % 2 == 0

number = int(input("Enter a number: "))

if powerof4(number):
    print(number, "is a power of 4")
else:
    print(number, "is not a power of 4")