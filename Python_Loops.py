#Exercise 01 - Simple While Loop

x = 0 #Initializing - Giving an initial value to a variable.
while x<5: 
    print("Not there yet, x=" + str(x))
    x = x+1
print("x=" + str(x))

#Exercise 02 - While loop inside a function

def attempts(n): 
    x = 1
    while x <= n:  
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5) 


#Exercise 03

def count_down(start_number):
    current = 3
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

count_down(3)


#Exercise 04

def print_range(start, end):
    	# Loop through the numbers from start to end
 
    n = start
    while n <= end:
        print(n)
        n+=1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 


#Exercise 05 -  Make the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):
      # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
    # Check if factor is a divisor of number
        if number % factor == 0:
      # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
        # If it's not, increment the factor by one
            factor += 1
    return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


#Exercise 06 - Avoiding an infinite loop.

def is_power_of_two(n):
      # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False