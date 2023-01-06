"""Brute Force
"""
a = [-2, 2, 5, -11, 6]
b = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
max_so_far, max_ending_here = float("-inf"), a[0]
for i in range(0, len(a)):
    max_ending_here = max_ending_here + a[i]
    if max_so_far < max_ending_here:
        max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
print(max_so_far)


"""Kadane's Algorithm
"""
max_sum = a[0]
current_sum = max_sum
for i in range(1, len(a)):
    current_sum = max(a[i] + current_sum, a[i])
    max_sum = max(current_sum, max_sum)
print(max_sum)
