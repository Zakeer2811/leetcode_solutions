class Solution:
    def minMaxDifference(self,num: int) -> int:
        s = str(num)

        # Get the maximum number
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num  # already all 9s

        # Get the minimum number
        for ch in s:
            if ch != '0':
                min_num = int(s.replace(ch, '0'))
                break
        else:
            min_num = num  # already all 0s?

        return max_num - min_num
