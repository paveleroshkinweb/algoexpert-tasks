from collections import defaultdict

# Time complexity - O(n)
# Space complexity - O(k), where k - number of teams
def tournamentWinner(competitions, results):
    points = defaultdict(lambda: 0)
    winner = competitions[0][0]
    for competition, result in zip(competitions, results):
        idx = (result + 1) % 2
        points[competition[idx]] += 1
        if points[winner] < points[competition[idx]]:
            winner = competition[idx]
    return winner