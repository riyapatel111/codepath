#advanced problem set version 1

# problem 1 -------------------------------------------------------------------------------------------------------
def transpose(matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        output = [[0]*rows for _ in range(cols)]
                  
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                return output

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = transpose(matrix)
for row in transpose:
     print(row)

# problem 2 -------------------------------------------------------------------------------------------------------

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]

        left += 1
        right -= 1


lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)

print(lst)

# problem 3 -------------------------------------------------------------------------------------------------------
def remove_dupes(items):
    """
    iterate through length of array -1
    if elem at i = elem at i +1
        remove elem at i
    """
    index = 0
    while index < len(items) - 1:
        if items[index] == items[index + 1]:
            items.pop(index)
            index -= 1
        index += 1

    return len(items)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "extract of malt", "extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))
 
# problem 4 -------------------------------------------------------------------------------------------------------
def sort_by_parity(nums):

    """
    * everytime there is a even number, send to beginning
    * keep relative order 
    even list and odd list
    for each num in nums 
        if even, add to even array
        if odd, add to odd array
    append odd array onto even (return even + odd)
    """

    even = []
    odd = []
    for num in nums:
        if num % 2 == 0: # even 
            even.append(num)
        else: 
            odd.append(num)

    return even + odd


nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))