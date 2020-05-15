class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.heap = points[:K]
        self.build_heap(self.heap)

        for i in range(K, len(points)):
            pt = points[i]
            top = self.heap[0]
            if pt[0] ** 2 + pt[1] ** 2 <= top[0] ** 2 + top[1] ** 2:
                self.heap[0] = pt
                self.heapify_down(self.heap, 0)

        return self.heap
    
    def build_heap(self, heap):
        i = (len(heap) - 2) // 2
        while i >= 0:
            self.heapify_down(heap, i)
            i -= 1

    def heapify_down(self, heap, i):
        n = len(heap)
        while i < n:
            child = -1
            m = heap[i][0] ** 2 + heap[i][1] ** 2
            if 2*i + 1 < n:
                d = heap[2*i + 1][0] ** 2 + heap[2*i + 1][1] ** 2
                if d >= m:
                    child = 2*i + 1
                    m = d
            if 2*i + 2 < n:
                d = heap[2*i + 2][0] ** 2 + heap[2*i + 2][1] ** 2
                if d >= m:
                    child = 2*i + 2
                    m = d
            if child != -1:
                heap[i], heap[child] = heap[child], heap[i]
                i = child
            else:
                break
