def length_of_string(word):
	return len(word)
	
def first_last_two(word):
    if len(world) < 2:
        print (word [:2] + word [-2])
    return ""	
	
def add_extra_word(word):
	if word[-3:] == "ing":
		return word+"ly"
	if len(word) >= 3:
		return word+"ing"
	if len(word) < 3:
		return word	
	
	
def longest_word_and_length_in_list(word):

	longest_word = word[0]
	longest_length = len(word[0])
	for content in word:
		if len(content) > highest_length:
			highest_length = len(content)
			highest_word = content


	print(highest_word, ",",highest_length, sep = "",end = "")
	return ""
			
def remove_odd_index(word):   
    result = ""    
    for index in range(len(word)):	
    if index % 2 != 0:            
        result += text[index]   
    return result
    
	    
def minimum_in_list(numbers):

	smallest_number = numbers[0]
	for number in numbers:
		if number < smallest_number:
			smallest_number = number
	return smallest_number



def maximum_in_list(numbers):

	highest_number = numbers[0]
	for number in numbers:
		if number > highest_number:
			highest_number = number
	return highest_number	
	
	
def string_number_repetion(word,number):
	if number.is_integer():
		return word * number
	else:
		return word

	
def list_square(numbers):
	squared_list = []
	for number in numbers:
		number = number ** 2
		squared_list.append(number)
	return squared_list

	
def sum_of_list_square(numbers):
	squared_list = []
	sum_of_number = 0
	for number in numbers:
		number = number ** 2
		squared_list.append(number)
	for number in squared_list:
		sum_of_number = sum_of_number + number
	return sum_of_number		
	
	
	
	
	
	
	
print(length_of_string("semicolon"))
print(first_last_two_world("semicolon"))
print(first_last_two_letter("on"))
print(first_last_two_letter("o"))
print(add_extra_word("abc"))
print(add_extra_word("string"))
print(add_extra_word("on"))
rint(longest_word_and_length_in_list(['welcome','out','weather','mobile','breakfast','journey']))
print(remove_odd_index("semicolon"))
print(minimum_in_list([8,4,9,2,5,7,3]))
print(maximum_in_list([8,4,9,2,5,7,3]))
print(string_number_repetion("hello",3))
print(string_number_repetion("hi",4.5))
print(list_square([2,3,4,5,7]))
print(sum_of_list_square([2,3,4,5,7]))
