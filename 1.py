# 1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myHashTable = HashTable(len(nums))

        for i in range(0,len(nums)):
            myHashTable.insert(nums[i],i)

        for i in range(0,len(nums)):
            if(myHashTable.getVal(target-nums[i]) and myHashTable.getVal(target-nums[i])!=i):
                return (i,myHashTable.getVal(target-nums[i]))
        
class HashTable:
    def __init__(self,size):
        self.size=size
        self.table = [[] for _ in range(size)]

    def HashFunction(self, key):
        return hash(key)%self.size

    def insert(self,key,value):
        index = self.HashFunction(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def getVal(self,key):
        index=self.HashFunction(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value if key is found
        return None  # Key not found
