from typing import List


class Solution:
    """
    kSmallestPairs find the k pairs with the smallest sums.
    """
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        li = []
        for n in nums1:
            for i in range(len(nums2)):
                li.append([n, nums2[i]])
        # Sort by sums with 0th element and 1st element added
        li.sort(key=lambda x: x[0]+x[1])
        return li[:k]
        

# Entry point for debug
if __name__ == "__main__":
    # nums1 = [1,7,11]
    # nums2 = [2,4,6]
    # k = 3

    # nums1 = [1,1,2]
    # nums2 = [1,2,3]
    # k = 2

    nums1 = [1,2,4,5,6]
    nums2 = [3,5,7,9]
    k = 3

    s = Solution()
    ans = s.kSmallestPairs(nums1=nums1, nums2=nums2, k=k)
    print(ans)