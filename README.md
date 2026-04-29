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

# Arrays
An array is a contiguous block of memory storing elements of the same type.
Key Features
Indexed (0-based)
Fixed order
Fast access
Can be static or dynamic (Python list, Java ArrayList)

Time & Space Complexity
Operation	Time Complexity
- Access (nums[i])	O(1)
- Update	O(1)
- Append (end)	O(1)*
- Insert (middle/front)	O(n)
- Delete (middle/front)	O(n)
- Search (unsorted)	O(n)
*Amortized

# Two Pointers
two indices to traverse a data structure, often an array or a linked list
these pointers can move in the same direction, opposite directions, or even in a sliding window fashion
reduces time complexity by avoiding nested loops

Variations:
- forward direction: both start at beginning and move towards the end
- opposite direction: one pointer starts at beginning and the other at end
- sliding window: one pointer moves faster than the other, creating a window of elements to process
**
Example 1: Two Sum (Sorted Array)**

Given a sorted array of integers, find two numbers that add up to a specific target. Using two pointers, one at the start and one at the end, we can efficiently find the pair in O(n) time.

def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

    
Example 2: Remove Duplicates from Sorted Array

Using two pointers, one to track the position of the next unique element, we can remove duplicates in-place.

def remove_duplicates(nums):
    if not nums: return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Sliding Window
problem solving technique that transforms two nested loops into one loop. It can reduce the time complexity of an algorithm to O(n).
Count Occurrences of Anagram
Solution 1

from collections import Counter

def isAnagram(s, word):
    return Counter(s) == Counter(word)

def countAnagram(text, word):
    w = len(word)
    count = 0
    d = {}

    if len(text) < w:
        return 0

    for i in range(len(text) - w + 1):
        ana = text[i:i + w]
        if ana not in d and isAnagram(ana, word):
            count += 1
            d[ana] = True

    return count

Solution 2:
def getCountOccurances(text, word):
    wHeap = [0] * 26
    textHeap = [0] * 26
    start = 0
    count = 0
    
    for c in word:
        wHeap[ord(c) - ord('a')] += 1
    
    for i in range(len(text)):
        textHeap[ord(text[i]) - ord('a')] += 1
        if (i - start + 1) == len(word):
            if textHeap == wHeap:
                count += 1
            
            textHeap[ord(text[start]) - ord('a')] -= 1
            start += 1
    return count


      
      
# Stacks

works like last-in-first-out
the most recent item goes out first
Core Stack Operations
- Push: add an element to the top of teh stack
- pop: remove the element from the top of the stack
- peek: look at the top element without removing it
- isEmpty: check if the stack has any elements
Implementation:
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0





# Binary Search
searching algorithm for finding an element's position in a sorted array.

Binary Search Algorithm
Iteration Method
do until the pointers low and high meet each other.
    mid = (low + high)/2
    if (x == arr[mid])
        return mid
    else if (x > arr[mid]) // x is on the right side
        low = mid + 1
    else                       // x is on the left side
        high = mid - 1
        
Recursive Method
binarySearch(arr, x, low, high)
    if low > high
        return False 
    else
        mid = (low + high) / 2 
        if x == arr[mid]
            return mid
        else if x > arr[mid]        // x is on the right side
            return binarySearch(arr, x, mid + 1, high)
        else                               // x is on the left side
            return binarySearch(arr, x, low, mid - 1)

Binary Search in Python
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if x == array[mid]:
            return mid

        elif x > array[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Linked List

data which denotes the value of the node.
next which is a reference to the succeeding node.

APPEND A NODE TO NON-EMPTY LINKED LIST
while (current.next != null) {
    current = current.next;
}
current.next = newNode;

How to Insert a node at the First Index
if (index == 0) {
    newNode.next = head;
    head = newNode;
}


How to Insert a Node at Any Position
for (int i = 0; i < index - 1 && current != null; i++) {
    current = current.next;
}
if (current != null) {
    newNode.next = current.next;
    current.next = newNode;
}

How to Delete a Node in a Linked List
if (index == 0) {
    deletedValue = head.data;
    head = head.next;
}


How to Delete a Node at a Given Position
for (int i = 0; i < index && current != null; i++) {
    previous = current;
    current = current.next;
}

if (current != null) {
    deletedValue = current.data;
    previous.next = current.next;
}
