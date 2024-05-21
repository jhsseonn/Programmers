### 내 답안
## 첫번째 시도
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs = []
        idx = 0
        while idx < len(nums):
            pairs.append([nums[idx], nums[idx+1]])
            idx += 2

        mins = []
        for i in range(len(pairs)):
            mins.append(min(pairs[i][0], pairs[i][1]))

        return sum(mins)

## 두번째 시도 - 정렬을 하면 굳이 순서쌍을 배열에 저장하고 저장된 순서쌍들 각각의 최솟값을 걸러내는 작업을 할 필요가 없음
## 실행 시간 단축
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mins = []
        idx = 0
        while idx < len(nums):
            mins.append(nums[idx])
            idx += 2

        return sum(mins)
