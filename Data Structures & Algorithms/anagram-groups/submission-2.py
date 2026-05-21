class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [[strs[0]]]
        for val in strs[1:]:
            is_inserted = False
            for i,ag in enumerate(ans):
                isanagram = self.check_anagrams(ag[0],val)
                if isanagram:
                    ans[i].append(val)
                    is_inserted = True
                    break
            if not is_inserted:
                ans.append([val])
        return ans
    
    def check_anagrams(self,str1: str,str2: str) -> bool:
        for val in str2:
            if val in str1:
                str1 = str1.replace(val,"",1)
            else:
                return False
        # print(str1)
        if str1 == "":
            return True
        else:
            return False
        