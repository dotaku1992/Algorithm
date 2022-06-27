def solution(arr1, arr2):
    answer = [[arr1[y][x]+arr2[y][x] for x in range(len(arr1[0]))] for y in range(len(arr1))]
    return answer