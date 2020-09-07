from typing import List
from collections import defaultdict


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            p = e.partition("@")
            local = p[0]
            if "." in local:
                local = p[0].replace(".", "")
            if "+" in local:
                local = local[:local.index("+")]
            addr = local + p[1] + p[2]
            s.add(addr)
        return len(s)
        

# Entry point for debug
if __name__ == "__main__":
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    s = Solution()
    ans = s.numUniqueEmails(emails=emails)
    print(ans)