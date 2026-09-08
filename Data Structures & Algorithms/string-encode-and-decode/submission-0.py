class Solution:

    def encode(self, strs: List[str]) -> str:
        val = ''
        for astr in strs:
            val += str(len(astr))
            val += '#'
            val += astr
        return val

    def decode(self, s: str) -> List[str]:
        words = []
        word = ''
        word_len_ch = ''
        word_len = 0
        s_len = len(s)
        i = 0
        while(i<s_len):
            if s[i] == '#':
                word_len = int(word_len_ch)
                word_len_ch = ''
                word = s[i+1:i+1+word_len]
                i = i+1+word_len
                words.append(word)
            else:
                word_len_ch += s[i]
                i+=1
        return words