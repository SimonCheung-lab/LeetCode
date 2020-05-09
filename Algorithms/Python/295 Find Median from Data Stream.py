import queue
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big_heap = []
        self.small_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        # print(type(num))
        if num is None:
            return

        self.count += 1
        if len(self.big_heap) == 0 or num <= self.big_heap[0]:
            self.big_heap.append(num)
            self.heapify_up(self.big_heap, len(self.big_heap), False, len(self.big_heap) - 1)
        else:
            self.small_heap.append(num)
            self.heapify_up(self.small_heap, len(self.small_heap), True, len(self.small_heap) - 1)
        
        # adjust
        if self.count % 2 == 0:
            if len(self.big_heap) > len(self.small_heap):
                tmp = self.big_heap[0]
                # insert one element into small heap, then heapify
                self.small_heap.append(tmp)
                self.heapify_up(self.small_heap, len(self.small_heap), True, len(self.small_heap) - 1)
                # delete heap top from big heap
                self.big_heap[0] = self.big_heap[-1]
                del self.big_heap[-1]
                self.heapify_down(self.big_heap, len(self.big_heap), False, 0)
            elif len(self.small_heap) > len(self.big_heap):
                tmp = self.small_heap[0]
                # insert one element into big heap, then heapify
                self.big_heap.append(tmp)
                self.heapify_up(self.big_heap, len(self.big_heap), False, len(self.big_heap) - 1)
                # delete heap top from small heap
                self.small_heap[0] = self.small_heap[-1]
                del self.small_heap[-1]
                self.heapify_down(self.small_heap, len(self.small_heap), True, 0)                 
        elif len(self.small_heap) > len(self.big_heap):
                tmp = self.small_heap[0]
                # insert one element into big heap, then heapify
                self.big_heap.append(tmp)
                self.heapify_up(self.big_heap, len(self.big_heap), False, len(self.big_heap) - 1)
                # delete heap top from small heap
                self.small_heap[0] = self.small_heap[-1]
                del self.small_heap[-1]
                self.heapify_down(self.small_heap, len(self.small_heap), True, 0)              

    def findMedian(self) -> float:
        if self.count == 0:
            return None
        
        if self.count % 2 == 1:
            return self.big_heap[0]
        else:
            return (self.big_heap[0] + self.small_heap[0]) / 2
    
    def heapify_up(self, heap, n, is_small, i):
        while i > 0:
            j = (i - 1) // 2
            if is_small:
                if heap[i] >= heap[j]:
                    break
            elif heap[i] <= heap[j]:
                break
            tmp = heap[i]
            heap[i] = heap[j]
            heap[j] = tmp
            i = j
    
    def heapify_down(self, heap, n, is_small, i):
        while i < n:
            left, right = i * 2 + 1, i * 2 + 2
            # leaf node
            if left >= n and right >= n:
                break

            j = left
            if is_small:
                if right < n and heap[right] < heap[left]:
                    j = right
                if heap[j] >= heap[i]:
                    break 
            else:
                if right < n and heap[right] > heap[left]:
                    j = right
                if heap[j] <= heap[i]:
                    break
            tmp = heap[i]
            heap[i] = heap[j]
            heap[j] = tmp
            i = j            
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
