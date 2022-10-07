# Time complexity - O(NlogN + MlogM)
# Space complexity - O(1)
def classPhotos(redShirtHeights, blueShirtHeights):
    if not redShirtHeights:
        return True
    redShirtHeights.sort()
    blueShirtHeights.sort()
    sign = redShirtHeights[0] > blueShirtHeights[0]
    return all(
        (redShirt >= blueShirt) is sign
        for redShirt, blueShirt in zip(redShirtHeights, blueShirtHeights)
    )