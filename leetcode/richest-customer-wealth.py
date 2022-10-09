# Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        temp = 0
        for account in accounts:
            tempSum = sum(account)
            if tempSum > temp:
                temp = tempSum
        
        return temp