# 1720. Decode XORed Array

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result=[first]
        for i in range(0,len(encoded)):
            result.append(encoded[i]^result[i])
        return result
