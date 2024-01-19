class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(List)

        for item in strs:
            counts = [0] * 26
            for c in item:
                counts[ord(c) - ord("a")] += 1

            key = str(counts)
            if key in groups:
                groups[key].append(item)
            else:
                groups[key] = [item]

        return groups.values()

        """
        The following solution has the time complexity O(mnlog(n))
        """

        # groups = {}
        # for item in strs:
        #     sorted_item = "".join(sorted(item))

        #     if sorted_item in groups:
        #         groups[sorted_item].append(item)
        #     else:
        #         groups[sorted_item] = [item]

        # return list(groups.values())
