class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        out = 0
        # part of assumption: if len(startTime != endTime)
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                out += 1
        return out


s = Solution()
print(s.busyStudent([1, 2, 3], [3, 2, 7], 4))
