# Time complexity - O(nlogn + mlogm)
# Space complexity - O(1)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    blueShirtSpeeds.sort()
    redShirtSpeeds.sort(reverse=fastest)
    total = 0
    for red, blue in zip(redShirtSpeeds, blueShirtSpeeds):
        total += max(red, blue)
    return total