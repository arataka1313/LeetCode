from typing import List

class Solution:
    def removeElement(self,nums:List[int],val: int) -> int:
        k = 0 #val以外の要素の数
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] 
                k += 1
        return k
    
def main():
    nums = [3,2,2,3]
    val = 3
    solution = Solution()
    k = solution.removeElement(nums, val)
    
    print("k =", k)
    print("valを除いたnums =",nums[:k])
    print("nums全体 =",nums)
    
if __name__ == "__main__":
    main()