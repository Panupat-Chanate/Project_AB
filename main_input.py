# from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import csv

Stop = 1
NumHuman = 1
Processing = 0
Human_list = []
List_Name = []
List_Age = []
List_Sex = []
List_Weight = []
List_Height = []

while Stop == 1:
    Name = input("\nInput Your Name (input 0 to stop) : ")

    if Name == '0':
        Stop = 0
        if len(Human_list) == 0:
            Processing = 0
        else:
            Processing = 1
    else:
        Stop = 1
        print("Hello " + str(Name))
        I_Age = input("Input Your Age : ")
        while I_Age.isnumeric() != True:
            I_Age = input("Input Your Age : ")

        I_Sex = str(input("Input Your Sex : ")).strip().lower()
        while I_Sex != 1 and I_Sex != 2:
            if I_Sex == 'male':
                I_Sex = 1
            elif I_Sex == 'female':
                I_Sex = 2
            else:
                I_Sex = str(input("Input Your Sex : ")).strip().lower()

        I_Weight = input("Input Your Weight : ")
        while I_Weight.isnumeric() != True:
            I_Weight = input("Input Your Weight : ")

        I_Height = input("Input Your Height : ")
        while I_Height.isnumeric() != True:
            I_Height = input("Input Your Height : ")

        Human_list.append([int(I_Age), int(I_Sex), int(I_Weight), int(I_Height)])
        List_Name.append(Name)
        List_Age.append(I_Age)
        List_Sex.append(I_Sex)
        List_Weight.append(I_Weight)
        List_Height.append(I_Height)
        NumHuman += 1

df_csv = pd.DataFrame(data={"Age": List_Age, "Sex": List_Sex, "Weight": List_Weight, "Height": List_Height})
df_csv.to_csv("data.csv", sep=',', index=False)

if Processing == 1:
    fileData = 'BigData.csv'
    data = pd.read_csv(fileData)

    data['Sex'] = data.Sex.replace(['F', 'M'], [2, 1])

    X = data[['Age', 'Sex', 'Weight', 'Height']]
    Y = data['Group']

    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.7, random_state=5)

    KNNmodel = KNeighborsClassifier(n_neighbors=3)
    KNNmodel = KNNmodel.fit(train_X, train_Y)
    KNNscore = KNNmodel.score(test_X, test_Y)
    result_predict = KNNmodel.predict(Human_list)

    print("ความแม่นยำ " + str(round(KNNscore, 2)*100) + "%")
    for i in range(len(result_predict)):
        print(List_Name[i]+" : "+result_predict[i])

    numThin = 0
    numSlim = 0
    numFat = 0
    for i in result_predict:
        if i == "FAT":
            numFat += 1
        elif i == "THIN":
            numThin += 1
        elif i == "SLIM":
            numSlim += 1
    y = [numFat, numThin, numSlim]
    x = ["FAT", "THIN", "SLIM"]
    # if numSlim < (numThin and numFat):
    #     exp = (0, 0, 0.1)
    # elif numThin < (numSlim and numFat):
    #     exp = (0, 0.1, 0)
    # elif numFat < (numSlim and numThin):
    #     exp = (numFat, numThin, numSlim)
    # else:
    #     exp = (0, 0, 0)
    plt.bar(x, y)
    plt.title("Body Mass Index : BMI")
    plt.show()

else:
    print("\n***** No People To Process *****")

