def is_leap(year):
        
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

year = int(input("Enter a year: "))

print(is_leap, year)

# Division in Python ever prints a float, even if the result is an integer.
x = 5/5
print(x)
# output: 1.0

# Division by Integer:
y = 10//3
print(y)
# output: 3