# Time complexity - O(m^h)
# Space complexity - O(h)
def staircaseTraversal(height, maxSteps):
    if height == 0:
        return 1
    if height < 0:
        return 0
    traverses = 0
    upperStep = min(height, maxSteps)
    for i in range(1, upperStep+1):
        traverses += staircaseTraversal(height-i, upperStep)
    return traverses
