"""
Program from a Hackerrank test question.
The program is given an array of strings as input.
Format includes location, month and amount of coffee consumed.
The program calculates the average and total consumed over a period of time.

Tip from some random youtube video: 
When in doubt, throw a hashmap (dictionary in Python) at the problem.
"""

def main(inputList):
    cityList = {}
    returnList = []

    for i in range(len(inputList)):
        temp = inputList[i].split(",")
        if temp[0] not in cityList:
            sum = int(temp[2])
            counter = 1
            cityList[temp[0]] = [sum, counter]
        else:
            updateStats = cityList[temp[0]]
            updateStats[0] += int(temp[2])
            updateStats[1] += 1
            cityList[temp[0]] = updateStats

    for i in cityList:
        calcAvg = cityList[i]
        calcAvg[1] = calcAvg[0] // calcAvg[1]
        cityList[i] = calcAvg
        returnList.append(i + "," + str(cityList[i][0]) + "," + str(cityList[i][1]))

    return returnList

inputList = ["Auckland,Jun,10",
"Auckland,Jul,10",
"Auckland,Aug,20",
"Auckland,Sep,15",
"Hamilton,Jan,10",
"Hamilton,Feb,5",
"Hamilton,Mar,30",
"Wellington,Apr,10",
"Wellington,May,10"]

results = main(inputList)
print(results)
