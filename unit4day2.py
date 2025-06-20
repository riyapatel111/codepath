# Problem Set Unit 4, Session 2, Version 1 Standard

#problem 1 -----------------------------------------------------------------------
def find_task_pair(task_times, available_time):
  # 2 ptr method
#   for i in range(len(task_times)):
#     for j in range(1, len(task_times)):
#       if task_times[i] 
    l, r = 0, len(task_times) - 1
    while l < r:
       total = task_times[l] + task_times[r]
       if available_time == total:
          return True
       elif available_time > total:
          # increment l
          l += 1
       else: # decrement
          r -= 1
    return False
task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))
task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))
task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))
# Example Output:
# True
# True
# False

#problem 2 -----------------------------------------------------------------------
def find_smallest_gap(work_sessions):
  # given list of tuple, start - end times
    min_diff = float('inf')
    for w in range(len(work_sessions)-1):
       # find difference
       # convert to mins
       end = work_sessions[w][1]
       start = work_sessions[w+1][0]
       # can convert to mins here
       diff = hhmm_to_mins(start) - hhmm_to_mins(end)
       # start - end # 1200 - 1130 = 70
       # compare diff
       if diff < min_diff:
          min_diff = diff
    # convert hours to min (ex: military time 1100)
    return min_diff
def hhmm_to_mins(hhmm):
   return (hhmm//100) * 60 + (hhmm%100)
       
work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions)) # 1500 - 1600 is 1 hour diff, so return 60
work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)] # its ret 70, should be 30 -> 1200 - 1130 = 70

#problem 3 -----------------------------------------------------------------------

def calculate_expenses(expenses):
    # create a dictionary to store totals for each category
    res, max, most_expensive = {}, 0, ""

    # iterate through list of tuple, key = [0], value = [1]
    for e in range(len(expenses)):
        res[expenses[e][0]] = res.get(expenses[e][0], 0) + expenses[e][1]

    # find max element

    for key, val in res.items():
        if val > max:
            max = val
            most_expensive = key

    return (res, most_expensive)
        

expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))

#problem 4 -----------------------------------------------------------------------
def word_frequency_analysis(text):
   freq = {}
   most_freq_word, occ = "", 0
   for word in text.split(" "):
       freq[word] = freq.get(word, 0) + 1
   for key, val in freq.items():
       if val > occ:
           occ = val
           most_freq_word = key
   return (freq, most_freq_word)

text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))