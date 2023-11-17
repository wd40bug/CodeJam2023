def findTriplets(nums, target):
    a=0
    b=0
    c=0
    triplets = []


    for a in range (len(nums) - 1):
        b = a + 1
        c = len(nums) - 1
        nums.sort()

        while(b < c): 
            if (nums[a] + nums[b] + nums[c]) == target: 
                triplets.append([nums[a], nums[b], nums[c]])
                b += 1
                c -= 1
            elif (nums[a] + nums[b] + nums[c]) > target: 
                c -=1
            else: 
                b += 1

    for (i, triple)  in enumerate(triplets):
        print(triple)


nums = [1, -2, 2, 0, -1]
target = 1
findTriplets(nums, target)
