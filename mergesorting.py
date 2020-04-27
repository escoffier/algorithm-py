from typing import List


def exchange(a, i: int, j: int):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def merge(a: List[int], lo: int, mid: int, hi: int):
    left: int = lo
    right: int = mid + 1
    b = a.copy()
    # print(b)

    print(left, right)
    print('############')
    for k in range(lo, hi + 1, 1):
        # print(right)
        # print(left)
        if left > mid:
            a[k] = b[right]
            right += 1
        elif right > hi:
            a[k] = b[left]
            left += 1
        elif b[right] < b[left]:
            a[k] = b[right]
            right += 1
        else:
            a[k] = b[left]
            left += 1
        print(left, right)
        print(a[k])


def sort(a: List[int], lo: int, hi: int):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    sort(a, lo, mid)
    sort(a, mid + 1, hi)
    merge(a, lo, mid, hi)


# 自底向上的归并，
def sort1(a: List[int]):
    N = len(a)
    aux = a[:]

    sz = 1
    while(sz < N):
        for lo in range(0, N- sz, 2*sz ):
            merge(a, lo, lo + sz - 1 , min(lo +  2*sz - 1, N -1) )
        print(a)
        sz = 2*sz

        


if __name__ == "__main__":
    # list1 = [1,5,9, 2, 4, 8 ]
    # mid:int = 5//2
    # merge(list1, 0, mid , 5)
    # print('###############')
    # print(list1)
    # print('###############')


    list2 = [3, 5, 34, 67, 68, 89, 93, 1, 4, 9, 11, 54, 71, 99, 44]
    merge(list2, 0, 6, 13)
    print(list2)

    list3 = [4, 3]
    merge(list3, 0, 0, 1)
    print(list3)

    # list2 = list1[:]
    # print(id(list1))
    # print(list1)
    # print(id(list2))
    # print(list2)
