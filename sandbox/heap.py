"""
implement Heap data structure.

https://github.com/drken1215/book_algorithm_solution/blob/master/codes/chap10/code_10_5.cpp
"""


class Heap:
    def __init__(self) -> None:
        self.heap = []
    
    def push(self, x: int) -> None:
        """
        push heap
        """
        self.heap.append(x)
        # x index
        xi = len(self.heap) - 1
        
        while xi>0:
            # parent index
            pi = (xi-1) // 2
            # check conpare value
            if self.heap[pi] > self.heap[xi]:
                break
            # move parent value to xi index.
            self.heap[xi] = self.heap[pi]
            xi = pi
        self.heap[xi] = x
    
    def pop(self):
        """
        pop heap
        """
        # 最後尾の要素をrootに格納する。
        x = self.heap.pop(-1)
        self.heap[0] = x        

        i = 0
        # leafにたどり着くまで
        while 2*i+1 < len(self.heap):
            l = 2*i+1
            r = 2*i+2
            c = r if r < len(self.heap) and self.heap[r] > self.heap[l] else l
            if self.heap[c] < self.heap[i]:
                break
            # change value
            self.heap[i] = self.heap[c]
            i = c
        self.heap[i] = x


if __name__ == "__main__":
    h = Heap()
    h.push(5)
    h.push(3)
    h.push(7)

    h.pop()
