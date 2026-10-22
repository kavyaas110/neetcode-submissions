class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha_count = {}
        left = 0
        right = 0
        best = 0
        alpha_count[s[right]] = alpha_count.get(s[right],0) + 1
        while right != len(s) and left <= right:
            window_len = right-left + 1
            max_count = max(alpha_count.values())
            # print(max_count, window_len, s[left:right+1])
            # print(alpha_count)
            if window_len - max_count <= k:
                if window_len > best:
                    # print(s[left:right+1],window_len)
                    best = window_len
                right += 1
                if right < len(s):
                    alpha_count[s[right]] = alpha_count.get(s[right],0) + 1
            else:
                alpha_count[s[left]] = alpha_count[s[left]] - 1
                if alpha_count[s[left]] == 0:
                    alpha_count.pop(s[left])
                left += 1
        
        return best