
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
    
    
def factor_Of(number):
        count = 0
    for i in range (1,number + 1):
       
        if (number % i == 0):
            count += 1
        return True




result1 = is_Even(10)		
result2 = is_prime_Number(7)		
result3 = subtract(3,7)		
result4 = divide(10,2)
result5 = factor_Of(10)






print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
