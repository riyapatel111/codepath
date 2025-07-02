#advanced problem set version 1

#problem 1 -------------------------------------------------------------------------------------------------------
def total_treasures(treasure_map):
    return sum(treasure_map.values())

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

treasure_map3 = {}

print(total_treasures(treasure_map1))
print(total_treasures(treasure_map2)) 
print(total_treasures(treasure_map3)) 

#problem 2 -------------------------------------------------------------------------------------------------------
def can_trust_message(message):
    counter = counter(message)
    return len(counter) >= 26 #at least 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))

#problem 3 -------------------------------------------------------------------------------------------------------
def find_duplicate_chests(chests):
    n = len(chests)
    appear = set()
    store_res = []
    for chest in chests:
        if chest not in appear:
            appear.add(chest)
        else:
            store_res.append(chest)
    return store_res
    
    counter = Counter(chests)
    return [num for num in counter if counter[num] == 2]

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

#problem 4 -------------------------------------------------------------------------------------------------------
from collections import Counter
def is_balanced(code):
    # code = arghh
    counter = Counter(code)
    # counter = {'a': 1, 'r': 1, 'g': 1, 'h': 2}
    arr_values = dict(counter).values()
    # arr_values = [1, 1, 1, 2]
    counter_values = Counter(arr_values)
    """
    counter_values = {1: 3, 2: 1} has 2 values (a and a + 1), 
    counter_values[a + 1] = 1
    """
    arr_counters = dict(counter_values).values()
    # arr_counters = [3, 1] 
    return list(arr_counters) == [len(arr_values) - 1, 1]

"""
arghh -> {'a': 1, 'r': 1, 'g': 1, 'h': 2}
argh -> {'a': 1, 'r': 1, 'g': 1, 'h': 1}

hahah -> {'h': 3, 'a': 2}
haha -> {'h': 2, 'a': 2}
"""

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2))

#problem 5 -------------------------------------------------------------------------------------------------------
#Given an array of integers gold_amounts representing the amount of gold at each location and an integer target, return the indices of the two locations whose gold amounts add up to the target.
#2 sum problem

def find_treasure_indices(gold_amounts, target):
    for i in range(len(gold_amounts)):
        for j in range(i + 1, len(gold_amounts)):
            if gold_amounts[i] + gold_amounts[j] == target:
                return [i, j]


gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  