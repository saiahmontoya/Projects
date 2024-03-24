
import sys
import heapq

class Solution:
    def minHeap(arr, k):
        heap_size = len(arr)
        heap = []
        # if k is out of bounds, raise value error
        if k <= 0 or k > heap_size:
            raise ValueError("k must be between 1 and", heap_size ,", inclusive")

        # lowest element in index is compared to num, if larger its popped to top of heap
        for num in arr:
            if len(heap) < k:
                heapq.heappush(heap, -num)
            else:
                # number is less than position 1, pop the integer
                if num < -heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -num)

        # max-heap to keep track of the k smallest elements
        return -heap[0]

    # Please make your function call as
    # PA2_yourname.py 2,3,4,5 4

def main():
    arr = [int(x) for x in sys.argv[1].strip("[]").split(",")]
    k = int(sys.argv[2])
    obj = Solution
    kth = obj.minHeap(arr, k)
    print(kth)

if __name__ == "__main__":
    main()



