from typing import List

def swap(a: List[int], i:int, j:int):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def quicksort(a: List[int], lo:int, hi:int):
    if lo < hi:
        p = partition(a, lo, hi)
        quicksort(a, lo, p - 1)
        quicksort(a, p + 1, hi)


def partition(a: List[int], lo:int, hi:int):
    pivot = a[hi]
    i = lo
    #left part of i is less than pivot
    for j  in range(lo, hi + 1, 1):
        print(f"i : {i}, j :{j}")
        #exchange j to left part
        if a[j] < pivot:
            swap(a, i, j)
            #i is less than pivot after exchanging now, so move forward
            i = i + 1
    swap(a, i, j)
    print(a)
    return i


def quicksort1(a: List[int], lo:int, hi:int):
    if lo < hi:
        p = partition1(a, lo, hi)
        quicksort(a, lo, p)
        quicksort(a,p + 1, hi)

def partition1(a: List[int], lo:int, hi:int):
    pivot = a[(lo + hi)//2]
    i = lo -1
    j = hi + 1

    while True:
        i = i + 1
        while a[i] < pivot:
            i = i + 1
        j = j -1
        while a[j] > pivot:
            j = j - 1

        if i >= j:
            return j
        swap(a, i, j)
            
        


if __name__ == '__main__':
    # main()
    # a  = [4,2,5,6,1,3, 9]
    # print(len(a))
    # quicksort1(a, 0, len(a) - 1)
    # print(a)

    # print('b******************b')
    # b = [1,2,3,4,5,6]
    # quicksort1(b, 0, len(b) - 1)
    # print(b)


    print('******************')
    c= [6,5,4,3,2,1]
    quicksort1(c, 0, len(c) - 1)
    print(c)

    d= [3,2]
    quicksort1(d, 0, len(d) - 1)
    print(d)
    