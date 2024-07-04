class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i+1, n):
                # the second condition checks if the first two numbers have leading zeros 
                if num[0] == "0" and i > 1:
                    break
                if num[i] == "0" and j > i + 1:
                    break

                num1= int(num[:i])
                num2= int(num[i:j])
                k = j
                while k < n:
                    num3 = num1 + num2
                    if num[k:].startswith(str(num3)):
                        k += len(str(num3))
                        num1 = num2
                        num2 = num3
                    else:
                        break
                if k == n:
                    return True

        return False