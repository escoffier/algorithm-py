from typing import List
from typing import Tuple

def str_sorting(a:List[Tuple]):
    print('统计频率')
    count = [0, 0, 0, 0,0,0]
    for word in a:
        count[word[1] + 1] +=1

    for i in count:
        print(i)

    print('将频率转换为索引')
    R = 5
    for r in range(R):
        count[r + 1] += count[r]
        # print(count[r ])
    for i in count:
        print(i)


    print('将元素分类')
    aux = a.copy()
    for w in  a:
        pos = count[w[1]]
        aux[pos] = w
        print( f"positon: {pos} , element: {w}")
        count[w[1]] +=1

    # for j in range(len(aux)):
    #     print(aux[j])
    for w in aux:
        print(w)
        
def test(parameter_list):
    aux = []
    aux.insert(3, ('Anderson', 2))
    aux.insert(8, ('Brown', 3))
    aux.insert(9, ('Davis', 3))
    aux.insert(14, ('Garcia', 4))
    aux.insert(0, ('Harris', 1))
    aux.insert(10,('Jackson', 3))
    aux.insert(15, ('Johnson', 4))
    aux.insert(11,('Jones', 3))
    aux.insert(1,('Martion', 1))
    aux.insert(4,('Martinez', 2))
    aux.insert(5,('Miller', 2))
    aux.insert(2, ('Moore', 1))
    aux.insert(6, ('Robinson', 2))
    aux.insert(16, ('Smith', 4))
    aux.insert(12, ('Taylor', 3))
    aux.insert(17, ('Thomas', 4))
    aux.insert(18, ('Thompson', 4))
    aux.insert(7, ('White', 2))
    aux.insert(13, ('Williams', 3))
    aux.insert(19,   ('Wilson', 4))

    # for w in aux:
    #     print(w)
    i = 0
    while(i < len(aux)):
        print(aux[i])
        i += 1
    b = aux.copy()
    print(id(aux))
    print(id(b))

if __name__ == "__main__":
    word_set = [('Anderson', 2)]
    # word_set.append(('Anderson', 2))
    word_set.append(('Brown', 3))
    word_set.append(('Davis', 3))
    word_set.append(('Garcia', 4))
    word_set.append(('Harris', 1))
    word_set.append(('Jackson', 3))
    word_set.append(('Johnson', 4))
    word_set.append(('Jones', 3))
    word_set.append(('Martion', 1))
    word_set.append(('Martinez', 2))
    word_set.append(('Miller', 2))
    word_set.append(('Moore', 1))
    word_set.append(('Robinson', 2))
    word_set.append(('Smith', 4))
    word_set.append(('Taylor', 3))
    word_set.append(('Thomas', 4))
    word_set.append(('Thompson', 4))
    word_set.append(('White', 2))
    word_set.append(('Williams', 3))
    word_set.append(('Wilson', 4))
    word_set.append(('Robbie', 0))

  

    # print(word_set[1][1])

    str_sorting(word_set)
    print('##############')

    for w in word_set:
        print(w)

    
    
    # test("")