class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            counts_s = {}
            counts_t = {}

            for i in range(len(s)):
                counts_s[s[i]] = counts_s.get(s[i], 0) + 1
                counts_t[t[i]] = counts_t.get(t[i], 0) + 1

            for i in range(len(s)):
                if counts_s[s[i]] != counts_t.get(s[i], 0):
                    return False

            return True

        else:
            return False
