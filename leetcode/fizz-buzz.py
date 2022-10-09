class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = [str(i+1) for i in range(n)]
        for index, item in enumerate(answer):
            temp = index+1
            if (temp % 3 == 0 and temp % 5 == 0):
                answer[index] = 'FizzBuzz'
            elif (temp % 3 == 0):
                answer[index] = 'Fizz'
            elif (temp % 5 == 0):
                answer[index] = 'Buzz'
        return answer