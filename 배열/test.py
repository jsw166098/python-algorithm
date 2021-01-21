nums = [1,2,3,4]

def productExceptSelf(nums):
    results = []
    mult = 1

    for i in nums:
        for j in nums:
            if i == j:
                continue
            mult *= j
        results.append(mult)
        mult = 1
    return results

print(productExceptSelf(nums))


