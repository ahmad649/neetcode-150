from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        master = {}
        for itm in strs:
            itm_sig = "".join(sorted(itm))
            if itm_sig not in master:
                master[itm_sig] = []

            master[itm_sig].append(itm)
        return list(master.values())








