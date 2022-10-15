# Time complexity O(N)
# Space complexity O(1)
def validStartingCity(distances, fuel, mpg):
    starting_city = 0
    current_rest = fuel[0] * mpg - distances[0]
    for i in range(1, len(distances)):
        if current_rest < 0:
            starting_city = i
            current_rest = fuel[i] * mpg - distances[i]
        else:
            current_rest += fuel[i] * mpg - distances[i]
    return starting_city
