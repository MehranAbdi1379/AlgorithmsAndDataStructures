nums = [2, 3, 3, 7, 11, 54, 24, 45, 3, 15]
target = 35

for i in range(len(nums) - 1):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] == target and i != j:
            print(str(i) + " " + str(j))
