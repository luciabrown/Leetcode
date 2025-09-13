# 383. Ransom Note

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note=Counter(ransomNote)
        mag=Counter(magazine)
        for letter,frequency in note.items():
            if frequency>mag[letter]:
                return False
        return True
