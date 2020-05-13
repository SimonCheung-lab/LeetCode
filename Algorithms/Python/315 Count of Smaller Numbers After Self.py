import bisect

# solution 1: bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        sorted_list = []
        for n in nums[::-1]:
            i = bisect.bisect_left(sorted_list, n)
            sorted_list.insert(i, n)
            ans.append(i)
        return ans[::-1]

# solution 2: merge sort    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            i, j = 0, 0
            tmp = []
            while i < len(left) or j < len(right):
                if j == len(right) or i < len(left) and left[i][1] <= right[j][1]:
                    ans[left[i][0]] += j
                    tmp.append(left[i])
                    i += 1
                else:
                    tmp.append(right[j])
                    j += 1
            
            return tmp

        ans = [0] * len(nums)
        arr = [(i, n) for i, n in enumerate(nums)]
        merge_sort(arr)
        return ans    
