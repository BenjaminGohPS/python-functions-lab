# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.

def calculate_area_triangle(base, height):
    area = (base * height) / 2
    return area

# print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.

def simple_interest(principal, rate, time):
    calculate = (principal * rate * time) / 100

    if calculate.is_integer():
         return int(calculate)
    else:
        return calculate

# print('Exercise 2:', simple_interest(1000, 5, 2))
# print('Exercise 2:', simple_interest(1500, 3.5, 5))


# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.

def apply_discount(price, discount):
    price_after = price * (1 - (discount / 100))
    return int(price_after)

# print('Exercise 3:', apply_discount(100, 25))
# print('Exercise 3:', apply_discount(80, 10))


# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.

def convert_temperature(temp, unit):
    if unit == 'C':
        return ((temp * 9/5) + 32) 
    else:
        return ((temp - 32) * 5/9) 


# print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
# print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.

def sum_to(n):
   
    return sum(range(n+1))    


# print('Exercise 5:', sum_to(6))
# print('Exercise 5:', sum_to(10))


# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.

def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


print('Exercise 6:', largest(1, 2, 3))
print('Exercise 6:', largest(10, 4, 2))



