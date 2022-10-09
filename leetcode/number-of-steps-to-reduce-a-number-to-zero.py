# Number of Steps to Reduce a Number to Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num/2
            else:
                num -= 1
            steps +=1 
            if num == 0:
                break
        return steps