# def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#     count = {}
#     freqency = [[] for i in range(len(nums) + 1)]

#     for n in nums:
#         count[n] = 1 + count.get(n, 0)
#     for n, c in count.items():
#             freqency[c].append(n)
    
#     answer = []
#     for i in range(len(freqency) - 1, 0, -1):
#            for n in freqency[i]:
#                   answer.append(n)
#                   if len(answer == k):
#                          return answer
# https://www.youtube.com/watch?v=YPTqKIgVk-k

def twoSum(nums: list[int], target: int) -> list[int]:
        numbers = []
        for i in nums:
            if i <= target:
                numbers.append(i)
        
        k = numbers[1]
        for n in numbers:
            if k + n == target:
                print(k , n)
                break
            else:
                k = numbers[2]
                continue

twoSum(nums =[2, 4, 10, 3, 4, 6, 4, 3, 2], target= 12)