from typing import List

class MyList:
    def __init__(self, parameter_list:List):
        self.vaules = parameter_list

    def __iter__(self):
        print('MyList::__iter__')
        return MyListIterator(self)

    def length(self):
        return len(self.vaules)

    def at(self, i:int):
        return self.vaules[i]

class MyListIterator:
    def __init__(self, myList:MyList):
        self.list = myList
        self.index = 0
        print('MyListIterator::__init__')

    def __iter__(self):
        print('__iter__()')
        return self

    def __next__(self):
        if self.index < self.list.length():
            print('__next__')
            result = self.list.at(self.index)
            self.index += 1
            return result
        raise StopIteration

if __name__ == "__main__":
    list1 = [5,4, 1, 2,6,9]
    list2 = MyList(list1)

    for i in list2:
        print(i)

    print('###########')
    ite = iter(list2) 
    for v in ite:
        print(v)
    # print(next(ite))