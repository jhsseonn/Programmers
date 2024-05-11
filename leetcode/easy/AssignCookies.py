class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result=0
        g.sort(reverse=True)
        s.sort(reverse=True)

        for i in range(len(g)):
            for j in range(len(s)):
                if g[i] <= s[j]:
                    s.remove(s[j])
                    result+=1
                    break

        return result

#중첩 for문을 사용하는 방법밖에 생각이 나지 않았다,,
#시간복잡도 줄이기
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0

        while i<len(g): #while문을 사용해 시간복잡도를 줄인다. while문은 중첩으로 사용하여도 시간복잡도가 심각하게 높아지지 않는다.
            while j<len(s) and g[i]>s[j]:
                j+=1
            if j==len(s): #쿠키를 모두 할당하면 while문을 빠져나간다.
                break
            i+=1
            j+=1
        return i
