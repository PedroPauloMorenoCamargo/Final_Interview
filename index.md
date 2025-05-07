# Final Interview

## Problem

**Amazon Top K Frequent Elements**

## Top K Frequent Elements

Given an integer array `nums`, return the **`k`** most frequent elements.  
You may assume that the answer is **unique**, meaning there will be no ties in frequency that affect the result — the `k` most frequent elements are clearly defined.    
Your algorithm's time complexity must be **better than O(n log n)**, where `n` is the array's length.

### Example


```python
Input: nums = [1,1,1,2,2,3,3,3,4,4,4,4], k = 3  
Output: [4, 1, 3]
```

Explanation:
- 4 appears 4 times  
- 1 and 3 appear 3 times  
- 2 appears only 2 times  
So the top 3 frequent elements are 4, 1, and 3.

Explanation:  
- `4` appears 4 times  
- `1` and `3` appear 3 times  
- `2` appears only 2 times  
So the top 3 frequent elements are `4`, `1`, and `3`.

### Constraints

- `1 <= nums.length <= 10⁵`  
- `-10⁴ <= nums[i] <= 10⁴`  
- `1 <= k <= number of unique elements in the array` 
- The result will always have **one valid answer** — no ambiguity due to ties in frequency.



---

## References

- [Top K Frequent Elements – NeetCode](https://neetcode.io/problems/top-k-elements-in-list)
- [Top K Frequent Elements - LeetCode ](https://leetcode.com/problems/top-k-frequent-elements/description/)
