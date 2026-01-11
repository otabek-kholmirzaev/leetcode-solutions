class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        max_area = 0

        def largestRectangleArea(heights):
            stack = []
            max_area_hist = 0
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area_hist = max(max_area_hist, height * width)
                stack.append(i)
            return max_area_hist

        for row in matrix:
            for j in range(m):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            max_area = max(max_area, largestRectangleArea(heights))

        return max_area