"""
735. Asteroid Collision

Add to List

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""
"""
Can't solve this problem without knowing while loop with continue, break and else statement
Check below link for reference:
https://realpython.com/python-while-loop/
"""


def collision_check(a_row):
    a_stack = []
    for a in a_row:
        while a_stack and a_stack[-1] > 0 > a:
            if abs(a_stack[-1]) < abs(a):
                a_stack.pop()
                continue  # Continue to next element in stack for comparison
            elif abs(a_stack[-1]) == abs(a):
                a_stack.pop()
            break  # while loop is ended by break, so else block won't execute and nothing will get appended to stack
        else:
            a_stack.append(a)  # while loop will break naturally by condition not being satisfied, new element will be appended to stack

    return a_stack

T = [[10,2,-5], [-2,-1,1,2], [8,-8], [5,10,-5]]
for t in T:
    print("In:", t, "Out:", asteroids(t))
