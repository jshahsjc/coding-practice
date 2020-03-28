"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

"""
Approach:
Brute force:
   Iterate through elements and get diff to rest of the elements if the next element is bigger than current element.
"""

def buySellStock(A):
   max_profit = 0
   for buy_index in range(len(A)):
      for sell_index in range(buy_index + 1, len(A)):
         if A[buy_index] < A[sell_index]:
            profit = A[sell_index] - A[buy_index]
            if profit > max_profit:
               max_profit = profit
               print "buy_index " + str(buy_index)
               print "sell_index " + str(sell_index)
               print "profit " + str(max_profit)
   return max_profit

I = [7,1,5,3,6,4]
I1 = [7,6,4,3,1]
print "Max profit " + str(buySellStock(I))
