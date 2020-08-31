from typing import List


class KthLargest:
    """
    Return kth largetst element in nums.
    add() is add val to nums, and return kth largetst element in nums.
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# Entry point for debug
if __name__ == "__main__":
    obj = KthLargest(3, [4,5,8,2])
    print(obj.add(3))   # returns 4
    print(obj.add(5))   # returns 5
    print(obj.add(10))  # returns 5
    print(obj.add(9))   # returns 8
    print(obj.add(4))   # returns 8