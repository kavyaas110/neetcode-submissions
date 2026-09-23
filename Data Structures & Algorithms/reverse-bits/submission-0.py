class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit_i = (n >> i) & 1
            res |= (bit_i<<(31-i))
        
        return res