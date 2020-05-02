# idea: find the max value, then divide the list from the max value index into two: left and right.
# The max area must be the sum of max left area and max right area.
# Notice the boundary condition.
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0 or max(height) == 0:
            return 0

        max_index = height.index(max(height))
        if max_index == 0:
            return self.get_right_area(max_index, len(height) - 1, height)
        if max_index == len(height) - 1:
            return self.get_left_area(0, max_index, height)

        return self.get_left_area(0, max_index, height) + self.get_right_area(max_index, len(height) - 1, height)
    
    def get_left_area(self, left, right, height):
        # height[right] is the max value
        if left >= right - 1:
            return 0

        # find the max value between [left, right - 1]
        if max(height[left: right]) == 0:
            return 0

        max_index = height[left: right].index(max(height[left: right])) + left
        # area between [max_index, right]
        area = height[max_index] * (right - max_index - 1) - sum(height[max_index + 1: right])
        return area + self.get_left_area(left, max_index, height)

    def get_right_area(self, left, right, height):
        # height[left] is the max value
        if left >= right - 1:
            return 0

        # find the max value between [left + 1, right]
        if max(height[left + 1: right + 1]) == 0:
            return 0
        
        max_index = height[left + 1: right + 1].index(max(height[left + 1: right + 1])) + (left + 1)
        # area between [left, max_index]
        area = height[max_index] * (max_index - left - 1) - sum(height[left + 1: max_index])
        return area + self.get_right_area(max_index, right, height)       
