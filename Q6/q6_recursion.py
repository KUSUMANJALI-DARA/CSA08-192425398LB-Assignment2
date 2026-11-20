
from functools import lru_cache
import sys

# Count calls for the simple recursive method
naive_calls = 0

def ways_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Count calls for the memoized method
memo_calls = 0

@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


# Iterative method
def ways_iterative(n):
    if n <= 1:
        return 1

    first = 1
    second = 1

    for i in range(2, n + 1):
        first, second = second, first + second

    return second


print("===== STAIRCASE RESULTS =====")

for n in range(1, 7):
    print("Steps:", n, "Ways:", ways_iterative(n))


print("\n===== RECURSIVE CALL COMPARISON =====")

for n in [10, 20, 25, 30]:
    naive_calls = 0
    memo_calls = 0
    ways_memo.cache_clear()

    naive_result = ways_naive(n)
    memo_result = ways_memo(n)

    print("\nNumber of steps:", n)
    print("Naive result:", naive_result)
    print("Naive function calls:", naive_calls)
    print("Memoized result:", memo_result)
    print("Memoized function calls:", memo_calls)


print("\n===== LARGE INPUT TEST =====")

n = 1000
print("Current recursion limit:", sys.getrecursionlimit())

ways_memo.cache_clear()

try:
    result = ways_memo(n)
    print("Memoized result for 1000 steps calculated.")
    print("Number of digits in result:", len(str(result)))
except RecursionError:
    print("RecursionError occurred for 1000 steps.")
    print("A loop-based solution avoids deep recursive calls.")

print("Iterative result for 1000 steps calculated.")
large_result = ways_iterative(1000)
print("Number of digits:", len(str(large_result)))
