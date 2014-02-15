# Write a function that takes an iterable 
#(something you can loop through, ie: string, list, or tuple) 
#and produces a dictionary with all distinct elements as the keys, 
#and the number of each element as the value
def count_unique(some_text):
    lower_text = some_text.lower()
    strip_text = lower_text.strip()
    split_text = strip_text.split()
    dictionary = {}
    for word in split_text:
        if not dictionary.get(word):
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    for key, value in dictionary.iteritems():
        print key, value


count_unique("Hello my name is Mitzi. Hello my dog's name is Timmy.")


# Given two lists, (without using the keyword 'in' 
#or the method 'index') return a list of all common items 
#shared between both lists
def common_items(list1, list2):
    new_list = []
    for word in list1:
        if word in list2:
            new_list.append(word)
    print new_list

common_items(['hello', 'my', 'name', 'is', 'Mitzi'], ['hello', 'my', 'hair', 'is', 'brown'])

# Given two lists, (without using the keyword 'in' or the 
#method 'index') return a list of all common items shared 
#between both lists. This time, use a dictionary as part of 
#your solution.
def common_items2(list1, list2):
    dictionary = {}
    

























