class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        currMax = 0
        m = 0
        n = len(height) - 1

        def area(i, j):
            return (j - i) * (min(height[i], height[j]))

        while n > m:
            currMax = max(currMax, area(m, n))
            if height[n] > height[m]:
                m += 1
            else:
                n -= 1

        return currMax
