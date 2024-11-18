''' Type your code here. '''
numbers = list(map(int, input().split()))
negative_nums = [num for num in numbers if num < 0]
negative_nums.sort(reverse=True)
print(*negative_nums, end=' ')