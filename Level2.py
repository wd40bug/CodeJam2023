def triplets(array, target):
    #while sum(arrays) < target:
        if (array[1] != array[0]) and (array[1] + array[0] < target):
            #var = position += 1
            triplets(var, target)


nums = [0,0,0,0]
target = 0
triplets(nums, target)
