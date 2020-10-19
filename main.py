from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

Restart = 1
Loop = []

while Restart == 1:
    Loop = input("File or Input: ").strip().lower()

    if Loop == 'file':
        numThin = 0
        numSlim = 0
        numFat = 0

        fileData = 'BigData.csv'
        inputData = 'NewData.csv'
        data = pd.read_csv(fileData)
        data2 = pd.read_csv(inputData)

        data['Sex'] = data.Sex.replace(['F', 'M'], [2, 1])
        # data2['Sex'] = data2.Sex.replace(['F', 'M'], [2, 1])

        X = data[['Age', 'Sex', 'Weight', 'Height']]
        Y = data['Group']

        train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.7, random_state=5)
        print(train_X.count())

        KnnModel = KNeighborsClassifier(n_neighbors=3)

        KnnModel = KnnModel.fit(train_X, train_Y)

        KnnScore = KnnModel.score(test_X, test_Y)
        print("ความแม่นยำ " + str(round(KnnScore, 2) * 100) + "%")

        df = pd.DataFrame(data2)
        print(df)
        print(df.to_numpy())

        newHuman = df.to_numpy()
        print(KnnModel.predict(newHuman))

        for i in KnnModel.predict(newHuman):
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
    elif Loop == 'input':
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
                while I_Age.isnumeric() != 1:
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
                while I_Weight.isnumeric() != 1:
                    I_Weight = input("Input Your Weight : ")

                I_Height = input("Input Your Height : ")
                while I_Height.isnumeric() != 1:
                    I_Height = input("Input Your Height : ")

                Human_list.append([int(I_Age), int(I_Sex), int(I_Weight), int(I_Height)])
                print(Human_list)
                List_Name.append(Name)
                List_Age.append(I_Age)
                List_Sex.append(I_Sex)
                List_Weight.append(I_Weight)
                List_Height.append(I_Height)
                NumHuman += 1

        df_csv = pd.DataFrame(data={"Age": List_Age, "Sex": List_Sex, "Weight": List_Weight, "Height": List_Height})
        df_csv.to_csv("NewData.csv", mode='a', header=False, sep=',', index=False)

        if Processing == 1:
            fileData = 'BigData.csv'
            data = pd.read_csv(fileData)

            data['Sex'] = data.Sex.replace(['F', 'M'], [2, 1])

            X = data[['Age', 'Sex', 'Weight', 'Height']]
            Y = data['Group']

            train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.7, random_state=5)

            KnnModel = KNeighborsClassifier(n_neighbors=3)
            KnnModel = KnnModel.fit(train_X, train_Y)
            KnnScore = KnnModel.score(test_X, test_Y)
            result_predict = KnnModel.predict(Human_list)

            print("ความแม่นยำ " + str(round(KnnScore, 2) * 100) + "%")
            for i in range(len(result_predict)):
                print(List_Name[i] + " : " + result_predict[i])

        else:
            print("\n***** No People To Process *****")