import sys
count = int(input().strip())
# print(count)

rlt = []
for i in range(count):
    nums = sorted(list(map(int, sys.stdin.readline().strip().split())))
    # print(nums)
    new_nums = sorted(list(set(nums)))

    # 1. 같은 눈 4
    if len(new_nums) == 1:
        rlt.append(50000 + new_nums[0]*5000)

    # 2. 같은 눈 3개 [1,1,1,2], [1,2,2,2]
    # 3. 같은 눈 2개가씩 두쌍 [1,1,2,2]
    elif len(new_nums) == 2:
        if nums[1] == nums[2]:
            rlt.append(10000 + nums[1]*1000)
        elif nums[1] != nums[2]:
            rlt.append(2000 + nums[0]*500 + nums[-1]*500)

    # 4. 같은 눈이 2개만 [1,1,2,3], [1,2,2,3], [1,2,3,3]
    elif len(new_nums) == 3:
        for i in new_nums:
            if nums.count(i) == 2:
                rlt.append(1000 + i*100)
                break

    # 5. 모두 다른 눈
    elif len(new_nums) == 4:
        rlt.append(new_nums[-1]*100)

print(max(rlt))