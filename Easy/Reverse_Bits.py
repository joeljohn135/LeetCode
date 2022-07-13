class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        stri=bin(n)
        stri=stri[2:]
        stri=stri[::-1] + ("0"*(32-len(stri)))
        return int(stri,2)
