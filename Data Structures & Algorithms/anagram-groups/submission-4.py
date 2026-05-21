class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hm = {}
        for val in strs:
            key = self.get_dictionary(val)
            print(key)
            if key not in hm:
                hm[key] = [val]
            else:
                hm[key].append(val)

        for key,value in hm.items():
            ans.append(value)
        return ans
    
    def get_dictionary(self,val: str) -> str:
        key = [0]*26
        for char in val:
            pos = ord(char) - ord('a')
            key[pos] = key[pos]+1
        key_str = ""
        for val in key:
            key_str += str(val) + "_"
        return key_str