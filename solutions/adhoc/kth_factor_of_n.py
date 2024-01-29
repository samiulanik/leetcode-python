# https://leetcode.com/problems/the-kth-factor-of-n/

def kthFactor(n: int, k: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
        if count == k:
            return i
    return -1
