# use a stack to first process the multiplication and division
# example:
# 3+2*2 = 3+4=7
# process until stack is empty


class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                if nums and nums[-1] in ('*', '/'):
                    op = nums.pop()
                    prev = nums.pop()
                    num = prev * num if op == '*' else int(prev / num)
                nums.append(num)
            else:
                nums.append(s[i])
                i += 1
        print(nums)

            
        result = nums[0]
        i = 1
        while i < len(nums):
            op = nums[i]
            num = nums[i + 1]
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            i += 2
        return result



