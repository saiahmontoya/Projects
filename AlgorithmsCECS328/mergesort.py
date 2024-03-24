

import sys
import random
import time

class Solution:

    # This function returns a descending sorted array.
    def function_a(self, elements_count: int) -> list:
        output = []
        for i in range(elements_count, 0, -1):
            output.append(i)
        return output

    # This function returns an ascending sorted array.
    def function_b(self, elements_count: int) -> list:
        output = []
        for i in range(1, elements_count + 1):
            output.append(i)
        return output

    def function_c(self, elements_count: int, seed: int):
        output = []
        random.seed(seed)
        for i in range(0, elements_count + 1):
            output.append(random.randint(1, 1000000))

        return output

    def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
        output = []
        if input_type == "a":
            output = self.function_a(elements_count)
        if input_type == "b":
            output = self.function_b(elements_count)
        if input_type == "c":
            output = self.function_c(elements_count, seed)
        return output

    # your merge sort algorithm comes here ...
    def pa1_mergesort(self, input_type: str, elements_count: int, seed: int) -> list:
        # your merge sort algorithm comes here ...
        sys.setrecursionlimit(10**6)
        output = []
        query_list = self.select_input(input_type, elements_count, seed)

        n = len(query_list)

        # get the start time
        st = time.process_time()

        def mergeSort(query_list):
            if len(query_list) > 1:
                mid = len(query_list) // 2
                left = query_list[:mid]
                right = query_list[mid:]

                #recursion
                mergeSort(left)
                mergeSort(right)

                i, j, k = 0, 0, 0

                #move value from left forward
                while i < len(left) and j < len(right):
                    if left[i] >= right[j]:
                        query_list[k] = left[i]
                        i = i + 1
                    else:
                        query_list[k] = right[j]
                        j = j + 1
                    k = k + 1

                #sort remaining    
                while i < len(left):
                    query_list[k] = left[i]
                    i = i + 1
                    k = k + 1
                while j < len(right):
                    query_list[k] = right[j]
                    j = j + 1
                    k = k + 1

                # end of merge sort

        mergeSort(query_list)
        et = time.process_time()
        res = et - st
        return [query_list, res]


if __name__ == '__main__':
    input_type = sys.argv[1]
    elements_count = int(sys.argv[2])
    seed = sys.argv[3]

    obj = Solution()
    ret = obj.pa1_mergesort(input_type, elements_count, seed)
    print(ret)
