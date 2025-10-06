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
  - Average O(n) expected overall (amortized O(1) per lookup/insert)
  - Worst:  O(n) in practice; pathological hashing aside
Space:
  - O(n) for the dictionary of seen values
Trade-off:
  - Extra memory to get linear time

  Time:
    - Best:   O(1) expected (match on first/second element)
    - Averag
def _run_tests():
    # Problem 1
    assert two_sum_bruteforce([2, 7, 11, 15], 9) in {(0, 1), (1, 0)}
    assert two_sum([2, 7, 11, 15], 9) in {(0, 1), (1, 0)}
    assert two_sum([3, 2, 4], 6) in {(1, 2), (2, 1)}
    try:
        two_sum([1, 2, 3], 100)
    except ValueError:
        pass

    # Problem 2
    assert is_anagram("listen", "silent") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("aabb", "baba") is True

    # Problem 3
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([], [1, 2]) == [1, 2]

    # Problem 4
    assert has_all_unique_chars("abc") is True
    assert has_all_unique_chars("abca") is False

    # Problem 5
    m = [[1,2,3],[4,5,6],[7,8,9]]
    rotate_matrix_90_inplace(m)
    assert m == [[7,4,1],[8,5,2],[9,6,3]]

    print("All tests passed.")

if __name__ == "__main__":
    _run_tests()
    Completed Assignment #5 with solutions and tests
