class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right, result = 0,0,0
        alpha_freq = {}
        
        for i,ch in enumerate(s):
            alpha_freq[ch] = alpha_freq.get(ch,0) + 1

            right = i
            window_size = right - left +1
            
            if window_size - max(alpha_freq.values()) <= k:

                result = window_size
            else:
                
                alpha_freq[s[left]] = alpha_freq.get(s[left],0) -1
                left +=1

        
        return result