class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sort the array
        citations.sort()
        h = 0
        flag = True
        for i in range(len(citations)):
            if citations[i] == 0:
                continue
            elif citations[i] and flag >= 1:
                h = 1
                flag = False
            elif len(citations)-i >= citations[i]:
                h = citations[i]
        return h
