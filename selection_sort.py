import sys

def selection_sort(values):
    sorted_list = [] #empty list with unsorted values
    for i in range (0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move)) #pops the minimum value and adds it to sorted list
    return sorted_list

def index_of_min (value):
    min = 0
    for i in range (1, len(value)):
        if value [i] < value[min]:
            min = i
    return min

numbers = [1, 3, 44, 112, 121,155,301,901,1]
print (selection_sort(numbers))
