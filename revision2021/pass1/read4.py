"""
https://leetcode.com/problems/read-n-characters-given-read4/
"""

def read(buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Number of characters to read (int)
    :rtype: The number of actual characters read (int)
    """
    buf4 = [' '] * 4
    buf = []
    rcount = 0
    b4cnt = 4

    while rcount < n:
        b4cnt = f.read4()
        # buf4 will store the read values
        for i in range(b4cnt):
            if rcount == n:
                return rcount
            buf.append(buf4[i])
            rcount += 1

    return rcount
