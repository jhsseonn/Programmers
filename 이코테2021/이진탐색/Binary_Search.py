# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 중간점 값과 타겟값이 같은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점이 타겟값 보다 큰 경우 끝점을 중간점 인덱스 바로 앞으로 바꿔서 재귀 호출
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점이 타겟값 보다 작은 경우 시작점을 중간점 인덱스 바로 뒤로 바꿔서 재귀 호출
    else:
        return binary_search(array, target, mid + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
