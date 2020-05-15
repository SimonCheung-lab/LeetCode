class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.small_heap = nums[:k]
        self.k = k
        self.build_heap()
        for i in range(k, len(nums)):
            if nums[i] >= self.small_heap[0]:
                self.small_heap[0] = nums[i]
                self.heapify_down(self.small_heap, 0)

    def add(self, val: int) -> int:
        if len(self.small_heap) == self.k:
            if val >= self.small_heap[0]:
                self.small_heap[0] = val
                self.heapify_down(self.small_heap, 0)
        else:
            self.small_heap.insert(0, val)
            self.heapify_down(self.small_heap, 0)

        return self.small_heap[0]        
            

    def build_heap(self):
        i = (self.k - 2) // 2
        while i >= 0:
            self.heapify_down(self.small_heap, i)
            i -= 1
    
    def heapify_down(self, heap, i):
        n = len(heap)
        while i < n:
            child = -1
            m = heap[i]
            if 2*i + 1 < n and heap[2*i + 1] < m:
                child = 2*i + 1
                m = heap[child]
            if 2*i + 2 < n and heap[2*i + 2] < m:
                child = 2*i + 2
            if child != -1:
                heap[i], heap[child] = heap[child], heap[i]
                i = child
            else:
                break


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
