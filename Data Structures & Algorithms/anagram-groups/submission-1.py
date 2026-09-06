class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqM = defaultdict(list)

        for ind, word in enumerate(strs):
            freq = [0] * 26
            for c in word:
                freq[ord(c)- ord('a')] +=1
            freqM[tuple(freq)].append(word)
        return list(freqM.values())

