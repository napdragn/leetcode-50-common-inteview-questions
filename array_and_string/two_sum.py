def twoSum(nums: list, target: int) -> tuple:
    visited = dict()
    for i, num in enumerate(nums):
        wanted_num = (target - num)
        if wanted_num in visited:
            return (i, visited[wanted_num])
        else:
            visited[num] = i
    return (-1, -1)