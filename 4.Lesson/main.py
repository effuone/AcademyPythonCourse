import string
import random
import collections

def get_random_string(length):
    choices = string.ascii_letters + string.digits
    random_string = [random.choice(choices)for\
        i in range(length)]
    return random_string

def get_indexes_of_symbols(str):
    dictionary = {}
    for i in range(0, len(str)):
        symbol = str[i]
        if(dictionary.get(symbol)):
            dictionary[symbol].append(i)
            continue
        dictionary.update({str[i]:[i]})
    return dictionary