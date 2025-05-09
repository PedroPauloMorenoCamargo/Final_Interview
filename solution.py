from typing import List
import heapq

# Sorting Approach
def topKFrequentSorting(self, nums: List[int], k: int) -> List[int]:
    # Create a dictionary to count the frequency of each number
    dictionary = {}
    # Count the frequency of each number in the list
    for number in nums:
        dictionary[number] = dictionary.get(number, 0) + 1
    # Convert the dictionary to a list of tuples (number, frequency)
    tuples = []
    # Sort the list of tuples based on frequency 
    for number, count in dictionary.items():
        tuples.append([count, number])
    # Sort the tuples based on frequency in descending order
    tuples.sort(reverse=True)
    # Create a list to store the top k frequent numbers
    res = []
    # Add the top k frequent numbers to the result list
    for i in range(0, k):
            res.append(tuples[i][1])
    return res


# Bucket Sort Approach
def topKFrequentBucket(self, nums: List[int], k: int) -> List[int]:
    # Create a dictionary to count the frequency of each number
    dictionary = {}
    # Count the frequency of each number in the list
    for number in nums:
        dictionary[number] = dictionary.get(number, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    # Create a list of buckets to store numbers based on their frequency
    for number, count in dictionary.items():
        buckets[count].append(number)
    # Create a list to store the top k frequent numbers
    res = []
    # Iterate through the buckets in reverse order (from highest frequency to lowest)
    for i in range(len(buckets) - 1, 0, -1):
        for number in buckets[i]:
            res.append(number)
            # If we have found k frequent numbers, return the result
            if len(res) == k:
                return res
    return res

# Min Heap Approach
def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
    # Create a dictionary to count the frequency of each number
    dictionary = {}
    # Count the frequency of each number in the list
    for number in nums:
        dictionary[number] = dictionary.get(number, 0) + 1
    # Create a min heap to store the top k frequent numbers
    heap = []
    # Iterate through the dictionary and add numbers to the heap
    for number, count in dictionary.items():
        heapq.heappush(heap, (count, number))
        # If the heap size exceeds k, remove the smallest element
        if len(heap) > k:
            heapq.heappop(heap)
    # Create a list to store the top k frequent numbers
    res = []
    # Add the numbers from the heap to the result list
    for count, number in heap:
        res.append(number)
    return res