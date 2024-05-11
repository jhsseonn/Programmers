# 힙큐 활용
# 힙큐 사용해 1부터 큐에 넣고 넣은 숫자들의 2배, 3배, 5배 되는 숫자들을 힙큐에 저장
# 최소힙 활용 -> 루트 노드가 가장 작은 값, 값이 작은 데이터가 우선적으로 제거
# 시간복잡도: O(NlogN)
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = []
        result = []
        heapq.heappush(h, 1)
        while len(result) < n:
            cur = heapq.heappop(h)
            if len(result) > 0 and result[-1]==cur:
                continue
            heapq.heappush(h, cur*2)
            heapq.heappush(h, cur*3)
            heapq.heappush(h, cur*5)
            result.append(cur)

        return result[-1]

# DP 활용
# 가장 작은 숫자를 기준으로 각각 2, 3, 5배인 숫자들을 배열에 넣은 후, 최솟값부터 배열에 추가
# n번째 오는 숫자가 정답
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1] #1은 기본으로 가장 먼저 들어가있는 숫자

        idx2 = 0
        idx3 = 0
        idx5 = 0

        while len(ans) < n:
            num = min(ans[idx2]*2, ans[idx3]*3, ans[idx5]*5)
            ans.append(num)

            if num==ans[idx2]*2: idx2+=1
            if num==ans[idx3]*3: idx3+=1
            if num==ans[idx5]*5: idx5+=1

        return ans[n-1]
