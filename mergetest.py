import unittest
from mergesorting import merge
from mergesorting import sort
from mergesorting import sort1

class TestSortingMethods(unittest.TestCase):
    def test_merge(self):
        list2 = [3, 5, 34, 67, 68, 89, 93, 1, 4, 9, 11, 54, 71, 99]
        lo = 0
        hi = len(list2) - 1
        mid = lo + (hi - lo)//2

        merge(list2, lo, mid, hi)
        print(list2)


    def test_sort1(self):
        print(" *******test_sort1")
        list1 = [11, 3, 4, 7, 6, 9, 2, 13, 5]
        sort(list1, 0,  8)
        print(list1)


    def test_sort2(self):
        print(" *******test_sort2")
        list3 = [3, 5, 34, 67, 68, 89, 93, 1, 4, 9, 11, 54, 71, 99, 44]
        sort(list3, 0,  len(list3) -1 )
        print(list3)

    def test_sort3(self):
        print(" *******test_sort3")
        list3 = [98, 2, 35, 24, 67, 87, 32, 1, 5, 3, 35, 76, 81, 45, 9]
        print(list3)

        sort1(list3 )
        print(list3)


if __name__ == "__main__":
    unittest.main()
