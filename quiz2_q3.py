numList = [1, 4, 2, 3, 5, 6, 1]
for value in numList:
    count = numList.count(value)
    if count > 1:
        result = "The list provided contains duplicate values."
        break
    else:
        result = "The list provided does not contain duplicate values."
print(result)
