class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        ans = 0
        for i in range(32):
            a_bit_i = (a>>i)&1
            b_bit_i = (b>>i)&1

            res = (a_bit_i ^ b_bit_i) ^ carry

            carry = (a_bit_i & b_bit_i) | ((a_bit_i | b_bit_i) & carry)

            ans = ans | (res<<i)

            if ans > (2**31)-1:
                ans = ~(ans^((2**32)-1))

        return ans

        