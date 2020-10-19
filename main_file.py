from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

fileData = 'BigData.csv'
testData = 'NewData.csv'
data = pd.read_csv(fileData)
data2 = pd.read_csv(testData)

data['Sex'] = data.Sex.replace(['F', 'M'], [2, 1])
data2['Sex'] = data2.Sex.replace(['F', 'M'], [2, 1])
print(data.head(10))

X = data[['Age', 'Sex', 'Weight', 'Height']]
Y = data['Group']

train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.7)
print(train_X.count())

Treemodel = tree.DecisionTreeClassifier()
KNNmodel = KNeighborsClassifier(n_neighbors=9)

#ให้มันเรียนรู้
Treemodel = Treemodel.fit(train_X, train_Y)
KNNmodel = KNNmodel.fit(train_X, train_Y)

TreeScore = Treemodel.score(test_X, test_Y)
KnnScore = KNNmodel.score(test_X, test_Y)
print("ความแม่นยำ " + str(round(TreeScore, 2)*100) + "%")
print("ความแม่นยำ " + str(round(KnnScore, 2)*100) + "%")
df = pd.DataFrame(data2)
print(df)
print(df.to_numpy())

newHuman = df.to_numpy()
print(KNNmodel.predict(newHuman))

numThin = 0
numSlim = 0
numFat = 0
for i in KNNmodel.predict(newHuman):
    print(i)
    if i == "FAT":
        numFat += 1
    elif i == "THIN":
        numThin += 1
    elif i == "SLIM":
        numSlim += 1
y = [numFat, numThin, numSlim]
x = ["FAT", "THIN", "SLIM"]
if numSlim < (numThin and numFat):
    exp = (0, 0, 0.1)
elif numThin < (numSlim and numFat):
    exp = (0, 0.1, 0)
elif numFat < (numSlim and numThin):
    exp = (numFat, numThin, numSlim)
else:
    exp = (0, 0, 0)
plt.pie(y, explode=exp, labels=x, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title("BMI")
plt.show()