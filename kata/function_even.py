
def is_Even(number):
    if (number % 2 == 0):
        return True
    else:
        return False

            					   
def is_prime_Number(number):    
    if number <= 1:  
        return False
        
    for i in range(2, number):
        if (number % i ==0 ):
            return False
            
        return True            
    
def subtract(first_number, second_number):
    if (first_number < second_number):
        return abs(first_number - second_number)
    else:
        return first_number - second_number
		
		
def divide(first_number, second_number):
    if (second_number == 0):
        return 0
    else:
        return first_number / second_number
    
    
def factor_of(number):
	for numbers in range(1,number + 1):
		if number % numbers == 0:
			print(numbers, end = " ") 
	return ""

def is_square(number):
	square_root = number ** (1/2)
	if number / square_root == int(square_root):
		return "true"
	else:
		return "false"
		
def is_palindrome(number):
	digit1 = number // 10000	
	digit2 = number // 1000 % 10
	digit3 = number // 100 % 10
	digit4 = number // 10 % 10 
	digit5 = number % 10
	
	if digit1 == digit5 and digit2 == digit4:
		return "true"
	else:
		return "false"
		
		
def factorial_of(number):
	product = 1
	for numbers in range(1,number + 1):
		product = product * numbers
	return product


def square_of(number):
	return number ** 2




result1 = is_Even(10)		
result2 = is_prime_Number(7)		
result3 = subtract(3,7)		
result4 = divide(10,2)
result5 = factor_Of(10)
result6 = (is_square(25))
result7 = (is_palindrome(54145))
result8 = (factorial_of(5))
result9 = (reuslt(square_of(12))







print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)


