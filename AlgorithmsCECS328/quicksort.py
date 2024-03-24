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

    # your quicksort algorithm comes here ...
    def pa1_quicksort(self, input_type: str, elements_count: int, seed: int) -> list:
        sys.setrecursionlimit(10**6)
        output = []
        query_list = self.select_input(input_type, elements_count, seed)

        n = len(query_list)

        # get the start time
        st = time.process_time()

        # CREATE PARITION
        def partition(query_list, left, right):
            #choose rightmost element as x/pivot
            pivot = query_list[right]
            i = left - 1
            #compare elements with pivot
            for j in range(left, right):
                if query_list[j] >= pivot:
                    #if pivot smaller, swap with greater element
                    i = i + 1

                    #swap i and j elements
                    (query_list[i], query_list[j]) = (query_list[j], query_list[i])
            (query_list[i + 1], query_list[right]) = (query_list[right], query_list[i + 1])
            #return poition
            return i + 1

        #performs quicksort algorithm
        def quicksort(ql, left, right):
            if left < right:
                #pivot element
                pi = partition(query_list, left, right)
                #recursion 
                quicksort(query_list, left, pi - 1)
                quicksort(query_list, pi + 1, right)

        quicksort(query_list, 0, n - 1)
        # end of quicksort

        et = time.process_time()
        res = et - st
        return [query_list, res]


if __name__ == '__main__':
    input_type = sys.argv[1]
    elements_count = int(sys.argv[2])
    seed = sys.argv[3]

    obj = Solution()
    ret = obj.pa1_quicksort(input_type, elements_count, seed)
    print(ret)