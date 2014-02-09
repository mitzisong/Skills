# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    for number in some_list:
        if number % 2 == 1:
            print number

all_odd(20)

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    for number in some_list:
        if number % 2 == 0:
            print number

all_even(20)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_words[]
    for word in word_list:
        if len(word) > 4:
            long_words.append(word)

    return long_words   

    long_words(['hi', 'hello', 'whatever'])
    

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest = some_list[0]
    for x in some_list:
        if x < smallest:
            smallest = x

    return smallest

smallest([2, 3, -1, 4, 9])

# Write a function that finddefs the largest element in a list of integers and returns it.
def largest(some_list):
    largest = some_list[0]
    for x in some_list:
        if x > largest:
            largest = x

    return largest
    
largest([3, 5, 1, 9, 100])        

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    new_list = []
    for x in some_list:
        half = float(x)/2
        new_list.append(half)
    return new_list

halvesies([2, 4, 6, 8])

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    word_lengths = []
    for word in word_list:
        word_length = len(word)
        word_lengths.append(word_length)
    return word_lengths

word_lengths(['one', 'a', 'something'])

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total = 0
        for num in numbers:
            total += num
    return total

sum_numbers([1, 2, 3, 4, 5])

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

mult_numbers([2, 2, 3])

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    string = ''
    for each in string_list:
            string += each
    return string

    join_strings(['the', 'cat', 'in', 'the', 'hat'])

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    total_numbers = len(numbers)
    total = 0
    for num in numbers:
        total += num
    return total/total_numbers

average([2, 4, 6, 8])