#unit 4 day 1 version 2

#problem 1 -----------------------------------------------------
def filter_meme_lengths(memes, max_length):
    result = []
    for meme in memes:
        if len(meme) <= max_length:
            result.append(meme)
    return result

memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]

print(filter_meme_lengths(memes, 20))
print(filter_meme_lengths(memes_2, 15))
print(filter_meme_lengths(memes_3, 10))

#problem 2 -----------------------------------------------------
def count_meme_creators(memes):
    hash = {}
    for meme in memes:  # Loop directly over the list
        if meme['creator'] in hash:
            hash[meme['creator']] += 1
        else:
            hash[meme['creator']] = 1
    return hash

memes = [
    {"creator": "Alex", "text": "Meme 1"},
    {"creator": "Jordan", "text": "Meme 2"},
    {"creator": "Alex", "text": "Meme 3"},
    {"creator": "Chris", "text": "Meme 4"},
    {"creator": "Jordan", "text": "Meme 5"}
]

memes_2 = [
    {"creator": "Sam", "text": "Meme 1"},
    {"creator": "Sam", "text": "Meme 2"},
    {"creator": "Sam", "text": "Meme 3"},
    {"creator": "Taylor", "text": "Meme 4"}
]

memes_3 = [
    {"creator": "Blake", "text": "Meme 1"},
    {"creator": "Blake", "text": "Meme 2"}
]

print(count_meme_creators(memes))
print(count_meme_creators(memes_2))
print(count_meme_creators(memes_3))

#problem 3 -----------------------------------------------------
def find_trending_memes(memes):
    count = {}
    result = []


    for meme in memes:
        if meme in count:
            count[meme] += 1
        else:
            count[meme] = 1

    for meme in count:
        if count[meme] > 1:
            result.append(meme)

    return result

memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(find_trending_memes(memes))
print(find_trending_memes(memes_2))
print(find_trending_memes(memes_3))

#problem 4 -----------------------------------------------------

def reverse_memes(memes):
    result = []
    for i in range(len(memes) - 1, -1, -1):
        result.append(memes[i])
    return result

#another way to do problem 4 using a stack

def reverse_memes(memes):
    left = 0
    right = len(memes) - 1

    while left < right:
        temp = memes[left]
        memes[left] = memes[right]
        memes[right] = temp
        left += 1
        right -= 1

    return memes



memes = ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(reverse_memes(memes))
print(reverse_memes(memes_2))
print(reverse_memes(memes_3))

#problem 5 -----------------------------------------------------

def find_trending_meme_pairs(meme_posts):
    #skipped this problem for now
    pass

#problem 6 -----------------------------------------------------
from collections import deque

def simulate_meme_reposts(memes, reposts):
    notempty = True

    while notempty:
        notempty = False
        for i in range(len(memes)):
            if reposts[i] > 0:
                reposts[i] -= 1 # decrement repost count
                notempty = True


memes = ["Distracted boyfriend", "Dogecoin to the moon!", "One does not simply walk into Mordor"]
reposts = [2, 1, 3]

memes_2 = ["Surprised Pikachu", "This is fine", "Expanding brain"]
reposts = [1, 2, 2]

memes_3 = ["Y U No?", "Philosoraptor"]
reposts = [3, 1]

print(simulate_meme_reposts(memes, reposts))
print(simulate_meme_reposts(memes_2, reposts))
print(simulate_meme_reposts(memes_3, reposts))