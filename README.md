# DSA_practice
Compilation of all DSA learning and LeetCode problems for analysis and understanding

All topics I want to cover over next 3 months (end data July 17th)
Data Structures:
- linked list
- arrays
- hash tables
- stack
- queue
- sorting

Algorithms
- 2 pointers
- sliding windows
- breadth-first search
- depth-first search
- backtracking
- heap
- binary search
- dynamic programming
- divide and conquer
- trie
- union find
- greedy


                Arrays
An array is a contiguous block of memory storing elements of the same type.
Key Features
Indexed (0-based)
Fixed order
Fast access
Can be static or dynamic (Python list, Java ArrayList)

Time & Space Complexity
Operation	Time Complexity
Access (nums[i])	O(1)
Update	O(1)
Append (end)	O(1)*
Insert (middle/front)	O(n)
Delete (middle/front)	O(n)
Search (unsorted)	O(n)
*Amortized

Basic Operations (Python)
Create
nums = [1, 2, 3, 4]
Access
print(nums[0])  # 1
Update
nums[1] = 10
Append / Insert
nums.append(5)        # end
nums.insert(1, 99)    # index insert
Delete
nums.pop()        # last
nums.pop(1)       # index
del nums[0]       # delete index

4. Traversal Techniques
A. Standard Loop
for i in range(len(nums)):
    print(nums[i])
B. Direct Iteration
for x in nums:
    print(x)
C. With Index + Value
for i, x in enumerate(nums):
    print(i, x)
5. Common Array Transformations
Reverse
nums.reverse()
# or
nums = nums[::-1]
Sort
nums.sort()          # ascending
nums.sort(reverse=True)
Copy
copy = nums[:]       # shallow copy

