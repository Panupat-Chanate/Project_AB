from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

fileData = 'BigData.csv'
data = pd.read_csv(fileData)

data['Sex'] = data.Sex.replace(['F', 'M'], [2, 1])
print(data.head(10))

X = data[['Age', 'Sex', 'Weight', 'Height']]
Y = data['Group']

train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.7, random_state=5)
print(train_X.count())

KNNmodel = KNeighborsClassifier(n_neighbors=3)

#ให้มันเรียนรู้
KNNmodel = KNNmodel.fit(train_X, train_Y)

KNNscore = KNNmodel.score(test_X, test_Y)

newHuman = [[60, 2, 79, 167], [67, 2, 54, 178], [23, 1, 45, 178]]
print(KNNmodel.predict(newHuman))