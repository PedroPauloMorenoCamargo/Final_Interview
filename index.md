# Final Interview

## Problem

**Amazon Top K Frequent Elements**


## Top K Frequent Elements

Given an integer array `nums`, return the **`k`** most frequent elements.  
You may assume that the answer is **unique**, meaning there will be no ties in frequency that affect the result — the `k` most frequent elements are clearly defined.    
Your algorithm's time complexity must be **better than O(n log n)**, where `n` is the array's length.



## Example


```python
Input: nums = [1,1,1,2,2,3,3,3,4,4,4,4], k = 3  
Output: [4, 1, 3]
```

Explanation:  
- `4` appears 4 times  
- `1` and `3` appear 3 times  
- `2` appears only 2 times  
So the top 3 frequent elements are `4`, `1`, and `3`.



## Constraints

- `1 <= nums.length <= 10⁵`  
- `-10⁴ <= nums[i] <= 10⁴`  
- `1 <= k <= number of unique elements in the array` 
- The result will always have **one valid answer** — no ambiguity due to ties in frequency.


## Hints

1. What’s the first step? We need to know how many times each number appears in the array. Is there a data structure that can help us count occurrences quickly?
2. Once we have the frequencies, how do we efficiently find the top `k` elements? Can we avoid sorting the entire list?
3. Heaps are great for retrieving top values efficiently. Could we use a min-heap of size `k` to track the most frequent elements as we go?
4. What if we wanted to do better? Could we group elements by frequency and then iterate from highest to lowest?
5. This problem has a clear upper bound on frequency — no number appears more than `n` times. Could we use this to our advantage with something like **bucket sort**?

---

## Solutions


### Sorting

A natural first approach is to count how often each number appears, then sort those counts and take the top `k`.

1. **Count Frequencies:**  
   First, we count the number of times each element appears in the input list. This can be done efficiently using a dictionary, which gives us a mapping of each number to its frequency in `O(n)` time.

2. **Sort by Frequency:**  
   Once we have the frequencies, we sort the list of `(frequency, element)` pairs in descending order by frequency. This step takes `O(n log n)` time due to the sort.

3. **Select Top `k`:**  
   Finally, we extract the first `k` elements from the sorted list. These are the `k` most frequent elements.

---

**Example:**

Suppose `nums = [1,1,1,2,2,3]`, and `k = 2`.

- Frequencies: `{1: 3, 2: 2, 3: 1}`
- Sorted by frequency in descending order: `[(3, 1), (2, 2), (1, 3) ]`
- Top 2 elements: `[1, 2]`

---

While this method works and is easy to implement, it doesn't meet the problem's constraint of being faster than `O(n log n)`. For that, we need a more efficient solution.




---

## References

- [Top K Frequent Elements – NeetCode](https://neetcode.io/problems/top-k-elements-in-list)
- [Top K Frequent Elements - LeetCode ](https://leetcode.com/problems/top-k-frequent-elements/description/)
