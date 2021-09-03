"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

def firstBadVersion(n):
    lo = 1
    hi = n
    if n == 0:
        return -1
    if n == 1 and if isBadVersion(n):
        return 1
    while lo <= hi:
        mid = lo + hi // 2
        if isBadversion(mid) and not isBadVersion(mid - 1):
            return mid
        elif not isBadversion(mid) and isBadVersion(mid + 1):
            return mid + 1
        elif isBadversion(mid):
            hi = mid - 1
        else:
            lo = mid + 1


def firstBadVersion(nums):
    if len(nums) > 1:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + hi // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    hi = mid - 1
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    lo = mid + 1
