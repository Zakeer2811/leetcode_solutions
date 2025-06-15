class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # Step to maximize the number (a)
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num  # all digits are 9

        # Step to minimize the number (b)
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for ch in s[1:]:
                if ch != '0' and ch != '1':
                    min_num = int(s.replace(ch, '0'))
                    break
            else:
                min_num = num  # all digits are 0 or 1

        return max_num - min_num
