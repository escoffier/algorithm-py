from typing import Any
from typing import List


class Node:
    def __init__(self):
        self.val = None
        self.next: Dict[str,Node] = {}


class TrieST:
    def __init__(self):
        self.R = 256
        self.root = Node()

    def put(self, key:str, value:Any):
        self.put1(self.root, key, value, 0)

    def put1(self, x:Node, key:str, value:Any,  d:int):
        print('###########')
        if x == None:
            print('new Node')
            x = Node()
        print(d)
        if d == len(key):
            x.val = value
            print(f'value: {x.val}')
            return x

        print(x.val)
        c = key[d]
        print(c)
        x.next[c] = self.put1(x.next.get(c), key, value, d + 1)
        return x

    def get(self, key:str) -> Any:
        node =  self.get1(self.root, key, 0)
        if node == None:
            return None
        return node.val
    
    def get1(self, node:Node, key:str, d:int) -> Node:
        if node == None:
            return None

        if d == len(key):
            return node

        c = key[d]
        return self.get1(node.next.get(c), key, d+1)

    def collect(self, node:Node, pre:str, q:List[str]):
        if node == None:
            return
        if node.val != None:
            q.append(pre)

        for k, v in node.next.items():
            self.collect(v, pre + k, q)

    def keyWithPrefix(self, pre:str):
        q = []
        self.collect(self.get1(self.root, pre, 0), pre, q)
        # for item in q:
        #     print(item)
        return q

    def keys(self):
        return self.keyWithPrefix('')

    def insert(self, key:str, value:Any):
        node = self.root
        for char in key:
            if char not in node.next:
                node.next[char] = Node()
            node  = node.next[char]

        node.val = value

            

if __name__ == "__main__":
    trie = TrieST()
    trie.put('she', 0)
    print('insert sells')
    trie.put('sells', 1)
    trie.put('sea', 2)
    #trie.put('by', 4)
    trie.insert('by', 4)

    print('get result:')
    v= trie.get('she')
    print(v)
    print(trie.get('sells'))
    print(trie.get('sea1'))

    # q= []
    # trie.collect(trie.root,  "sh" , q)
    pre = 'b'
    print(f"\nkeyWithPrefix {pre}")
    q = trie.keyWithPrefix(pre)
    if len(q) == 0:
        print(f'not found string with prefix {pre}')
        
    for item in q:
        print(item)
    
    print('\nkeys: ')
    q= trie.keys()
    for item in q:
        print(item)

    trie1 = TrieST()
    keys = { 'a':0, 'ab':1, 'bab':2, 'bc':3, 'bca':4, 'c':5, 'caa':6}

    for k, v in keys.items():
        trie1.put(k, v)
    q= trie1.keys()
    for item in q:
        print(item)
            
            
            
