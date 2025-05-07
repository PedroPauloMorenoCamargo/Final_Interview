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