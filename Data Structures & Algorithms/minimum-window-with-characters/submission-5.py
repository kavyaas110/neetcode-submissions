class Solution:
    def minWindow(self, s: str, t: str) -> str:
        set_t = set(t)
        hashset_t = {}
        window_hashset = {}
        for ch in t:
            hashset_t[ch] = hashset_t.get(ch,0)+1
        
        left = 0
        right = 0
        need = 0
        have = len(set_t)
        pop = False
        left_val = False
        best_so_far = len(s) + 1
        ans = (0,0)
        while (right < len(s)+1 and left < len(s)+1) or pop:
            if need == have:
                window_len = right - left
                if window_len < best_so_far:
                    best_so_far = window_len
                    ans = (left,right) 
                pop = True
            else:
                pop = False
            if pop:
                ch = s[left]
                if ch in set_t:
                    window_hashset[ch] = window_hashset[ch] - 1
                    if window_hashset[ch] < hashset_t[ch]:
                            need -= 1
                left += 1
            else:
                if not left_val:
                    if left >= len(s):
                        break
                    if s[left] in set_t:
                        ch = s[left]
                        window_hashset[ch] = window_hashset.get(ch,0) + 1
                        if window_hashset[ch] == hashset_t[ch]:
                            need += 1
                        left_val = True
                        right = left+1
                    else:
                        left += 1
                else:
                    if right >= len(s):
                        break
                    ch = s[right]
                    if ch in set_t:
                        window_hashset[ch] = window_hashset.get(ch,0) + 1
                        if window_hashset[ch] == hashset_t[ch]:
                            need += 1
                    right += 1
        return s[ans[0]:ans[1]]