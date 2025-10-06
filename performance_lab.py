"""
Assignment #5: Test, Analyze, Optimize — performance_lab.py

How to use this file
- Implementations for FIVE problems are below.
- After EACH function there’s a multiline comment with:
  * Best / Average / Worst time complexity
  * Space complexity
  * Optimization notes + trade-offs
- Problem 1 shows BOTH a brute-force and an optimized version (required “optimize one”).
- Tests are at the bottom. Run:  python performance_lab.py
"""

from typing import List, Dict, Tuple


# ------------------------------------------------------------
# Problem 1: Two Sum (return indices)
# ------------------------------------------------------------
def two_sum_bruteforce(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Return indices (i, j) with i<j such that nums[i] + nums[j] = target.
    Brute-force version kept for comparison with the optimized approach.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return i, j
    raise ValueError("No pair sums to target")


def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Optimized using a hash map of {value: index}.
    Returns the first valid pair of indices (i, j) found during a single pass.
    """
    seen: Dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    raise ValueError("No pair sums to target")


"""
Analysis (Problem 1 — Two Sum)

Brute-force:
  Time:
    - Best:   O(1) (first two elements already match)
    - Average O(n^2)
    - Worst:  O(n^2) (check all pairs)
  Space: O(1)
  Notes: Very simple but quadratic — poor scalability.

Optimized (hash map):
  Time:
    - Best:   O(1) expected (match on first/second element)
    - Averag
