def maxArea(height):
    l = 0
    r = len(height) - 1
    maxArea = 0

    while l < r:
        currArea = min(height[l], height[r]) * (r - l)
        if currArea > maxArea:
            maxArea = currArea

        if height[l] < height[r]:
            l += 1

        else:
            r -= 1

    return maxArea


height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height1))
height2 = [1, 1]
print(maxArea(height2))
err1 = [2, 3, 4, 5, 18, 17, 6]
print(maxArea(err1))
