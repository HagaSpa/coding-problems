from typing import List


class Solution:
    """
    intersection return intersection of nums1 and nums2.
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        ans = s1.intersection(s2)
        return ans


if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    s = Solution()
    ans = s.intersection(nums1=nums1, nums2=nums2)
    print(ans)