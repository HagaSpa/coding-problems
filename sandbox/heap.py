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


if __name__ == "__main__":
    h = Heap()
    h.push(5)
    h.push(3)
    h.push(7)
