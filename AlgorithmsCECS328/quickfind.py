
import sys
import random

# CREATE PARITION
def partition(query_list, left, right):
    #choose rightmost element as x/pivot
    pivot_index = random.randint(left, right)
    query_list[pivot_index], query_list[right] = query_list[right], query_list[pivot_index]
    #compare elements with pivot
    pivot_value = query_list[right]
    i = left - 1
    for j in range(left, right):
        if query_list[j] <= pivot_value:
            #if pivot smaller, swap with greater element
            i += 1
            #swap i and j elements
            query_list[i], query_list[j] = query_list[j], query_list[i]
    query_list[i + 1], query_list[right] = query_list[right], query_list[i + 1]
    #return poition
    return i + 1

#performs quicksort algorithm
def quicksort(query_list, left, right, k):
    if k > len(query_list) or k <= 0:
        raise ValueError("K must only be between 1 and ",len(query_list))
    #pivot element
    pi = partition(query_list, left, right)

    if pi > k:
        return quicksort(query_list, left, pi - 1, k)
    elif pi == k:
        return query_list[pi]
    else:
        return quicksort(query_list, pi + 1, right, k)

        

def kthSmallest(arr, k):
    # use quickselect to find the kth smallest element in the array
    return quicksort(arr, 0, len(arr) - 1, k - 1)

# Please make your function call as
# PA2_yourname.py 2,3,4,5 4

def main():
    array = [int(x) for x in sys.argv[1].strip("[]").split(",")]
    k = int(sys.argv[2])
    kth = kthSmallest(array, k)
    print(kth)

if __name__ == "__main__":
    main()
