# Bubble Sort

'''
Now that you know about how bubble sort works,
you'll implement bubble sort for two exercises.
'''

# Exercise 1
'''
Sam records when he/she wakes up every morning.
Assuming Sam always wakes up in the same hour,
use bubble sort to sort by earliest to latest.
'''


def bubble_sort_1(l):
    # TODO: Implement bubble sort solution
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index] = prev
            l[index -1] = this



wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]

bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")


#Exercise 2
'''
Sam doesn't always go to sleep in the same hour.
Given the following times Sam has gone to sleep,
sort the times from latest to earliest.
'''


def bubble_sort_2(l):
    for interation in range(len(l)):
        for index in range(1, len(l)):
            this_hour, this_min = l[index]
            prev_hour, prev_min = l[index - 1]

            if prev_hour > this_hour or (prev_hour == this_hour and prev_min > this_min):
                continue

            l[index] = (prev_hour, prev_min)
            l[index - 1] = (this_hour, this_min)

sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]
bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")
