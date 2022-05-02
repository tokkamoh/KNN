import math

yeastFileTrain = open(
    r"E:\Bioninformatics\year4,sem1\Machine Learning and Bioinformatics\Assignments\uci_datasets\yeast_training.txt")
yeastFileTest = open(
    r"E:\Bioninformatics\year4,sem1\Machine Learning and Bioinformatics\Assignments\uci_datasets\yeast_test.txt")

dataTrain = []
dataFloatListTrain = []
outputTrain = []
for line in yeastFileTrain:
    dataTrain.append(line.split())

for i in range(len(dataTrain)):
    dataFloatTrain = []
    for j in range(len(dataTrain[i])):
        if j == len(dataTrain[i]) - 1:
            outputTrain.append(int(dataTrain[i][j]))
        else:
            dataFloatTrain.append(float(dataTrain[i][j]))
    dataFloatListTrain.append(dataFloatTrain)

dataTest = []
dataFloatListTest = []
outputTest = []
for line in yeastFileTest:
    dataTest.append(line.split())

for i in range(len(dataTest)):
    dataFloatTest = []
    for j in range(len(dataTest[i])):
        if j == len(dataTest[i]) - 1:
            outputTest.append(int(dataTest[i][j]))
        else:
            dataFloatTest.append(float(dataTest[i][j]))
    dataFloatListTest.append(dataFloatTest)


# print(dataFloatListTest, "\n", outputTest)


def ecuDistance(train, test, outTrain):
    outDis = []
    for i in range(len(train)):
        out = 0
        for j in range(len(train[i])):
            out += ((train[i][j] - test[j]) ** 2)
        outDis.append([math.sqrt(out), outTrain[i]])
    outDis.sort()
    return outDis


def frequentClass(outDis):
    mV = 0
    currClassFrequency = []
    freDis = list(set(outDis))
    maxClass = []
    for i in freDis:
        currClassFrequency.append([outDis.count(i), i])
    # print(currClassFrequency)
    maxVal = max(currClassFrequency)
    # print(maxVal)
    for j in range(len(currClassFrequency)):
        if currClassFrequency[j][0] == maxVal[0]:
            maxClass.append(currClassFrequency[j][1])
    if len(maxClass) > 1:
        ind = []
        for i in maxClass:
            ind.append(outputTrain.index(i))
            mini = min(ind)
            mV = outputTrain[mini]
        return mV
    else:
        return maxVal[1]


# l = [1, 4, 1, 1, 3, 3, 4, 5, 6, 3, 4]
# print(frequentClass(l))

# print(ecuDistance(dataFloatList[:5], dataFloatList[5], output[:5]))
knn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# listDist = []
finClass = []
for i, j in enumerate(dataFloatListTest):
    disRes = ecuDistance(dataFloatListTrain, j, outputTrain)
    # listDist.append(disRes)
    outDisRes = []
    counter = 0
    for k in knn:
        classes = []
        for x in disRes[:k]:
            classes.append(x[1])
        outDisRes.append(frequentClass(classes))
    finClass.append(outDisRes)
print(finClass)

accuracy = []
for k in knn:
    match = 0
    print("k = ", k)
    for i, j in enumerate(finClass):
        print("Predicted class: ", j[k-1], "Actual Class: ", outputTest[i])
        if j[k-1] == outputTest[i]:
            match += 1
    accuracy.append((match/len(outputTest)) * 100)
    print("Matched outputs when k = ", k, "is: ", match)
    print("Accuracy when k = ", k, "is: ", accuracy[k-1])
