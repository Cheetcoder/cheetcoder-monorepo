---
title: Grokking the Coding Interview
description: This exercise will help you understand how we are using Grokking the coding interview
---

---
## Let's Code!

Instructions

Navigate to [https://designgurus.org/course/grokking-the-coding-interview](https://designgurus.org/course/grokking-the-coding-interview) and work through the problems in the sliding window section. 

---
## Sliding Window Template

Eventually you will realize that there is template you can use to generalize these problems: 

This is how I remember it, but your template might be different. 

### Easy Problems Template:
```python
def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        # slide the window, no need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K)  # calculate the average
            windowSum -= arr[windowStart]  # subtract the element going out
            windowStart += 1  # slide the window ahead

    return result
```

### Medium Problems Template:
- Same as above + they added a dictionary (hashmap)

```python
def fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        # shrink the sliding window, until we are left with '2' fruits in the fruit
        # frequency dictionary
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1  # shrink the window
        max_length = max(max_length, window_end-window_start + 1)
    return max_length
```



---
## Tracking Your progress

I am providing a few links on how I have historically tracked my progress.

- [Excalidraw.com](https://excalidraw.com/#json=5jh6QEP50RfJb1f35gtOS,VoyISZi40WIN6gd82Qlcbg) Example on how to use Excalidraw for daily coding.
- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1uKESRwdC-8KC9JI_lvLzqarbKPK5DJGHk0G5tW5zgFs/edit?usp=sharing) Tracking via an excel spreadsheet. Just clone it.

---
## Further Work 

If this is your second time going through this course I recommend take a stab at sliding window problems from the following course. Please prioritize the Grokking course first.

- [https://neetcode.io/practice](https://neetcode.io/practice)
- [https://seanprashad.com/leetcode-patterns/](https://seanprashad.com/leetcode-patterns/)



---
## Relevant Links

- [https://designgurus.org/course/grokking-the-coding-interview](https://designgurus.org/course/grokking-the-coding-interview)
-[https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions](https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions)
- [https://gist.github.com/tykurtz/3548a31f673588c05c89f9ca42067bc4](https://gist.github.com/tykurtz/3548a31f673588c05c89f9ca42067bc4)
- [https://github.com/dipjul/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions](https://github.com/dipjul/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions)
- [https://leetcode.com/problemset/all/?topicSlugs=sliding-window&page=1&sorting=W3t9XQ%3D%3D](https://leetcode.com/problemset/all/?topicSlugs=sliding-window&page=1&sorting=W3t9XQ%3D%3D)
