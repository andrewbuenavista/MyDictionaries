file = open("WorldSeriesWinners.txt", "r")

winners = file.read()

winners = winners.splitlines()

winnerCount = {}
winnerByYear = {}

for x in winners:
    winnerCount[x] = winners.count(x)

count = 1903

for x in winners:

    winner = []
    winner.append(x)
    winner.append(winnerCount[x])

    winnerByYear[int(count)] = winner
    count += 1

    if count == 1904 or count == 1994:
        count += 1


year = int(input("Please enter a year between 1903 and 2008 for the winner of that years World Series: "))

print(winnerByYear.get(year, "No winner for that year"))
