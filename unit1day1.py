#advanced problem set version 2

# problem 1 ------------------------------------------------------------------------------------------------------
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# problem 2 ------------------------------------------------------------------------------------------------------

def final_value_after_operations(operations):
    tigger = 1
    for op in operations:
        if op == "bouncy" or op == "flouncy":
            tigger += 1
        elif op == "trouncy" or op == "pouncy":
            tigger -= 1
    return tigger

# problem 3 ------------------------------------------------------------------------------------------------------
def tiggerfy(word):
    w = word
    w = w.replace("gg", "", 1)  # remove 'gg' once (as it's a pair)
    w = w.replace("GG", "", 1)
    w = w.replace("t", "").replace("T", "")
    w = w.replace("i", "").replace("I", "")
    w = w.replace("er", "").replace("ER", "").replace("Er", "").replace("eR", "")
    return w
