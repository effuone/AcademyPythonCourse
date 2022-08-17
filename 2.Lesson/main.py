import json
# a function that reverses given list
def reverse_list(input_list):
    input_list.reverse()
    return input_list

#a funcation that replaces first and last elements of list 
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

#a function that returns new tuple from starting index at random value and ending
def slicer(tup, randomValue):
    arr = []
    for i in range(0, len(tup)):
        if(tup[i]==randomValue):
            if(i==len(tup)):
                arr.append(tup[i])
                break
            while(tup[i+1]!=randomValue):
                arr.append(tup[i+1])
                i+=1
                if(i+1>=len(tup)):
                    break
            break
    return tuple(arr)

f = open('products.json')
data = json.load(f)['results']
for i in data:
    print(i['price'])