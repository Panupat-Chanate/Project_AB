import numpy as np
def knn(today):
    X = np.array([[22.8, 40], [20.3, 45], [18.2, 46], [19.6, 48],
            [24.1, 29], [17.8, 51], [17.7, 25], [28.6, 27]])
    Y = np.array(["No", "No", "Yes", "Yes",
            "Yes", "No", "Yes", "No"])
    Result = np.array(today)
    Dist = np.zeros(len(Y))

    for i, dataX in enumerate(X):
        Dist[i] = np.sqrt(np.sum((Result-dataX)**2))

    # ค่าที่น้อยที่สุด
    minDist = np.min(Dist)
    # ลำดับ
    indexMin = np.argmin(Dist)
    #
    predictResult = Y[indexMin]
    return minDist, indexMin, "ฝนตกไหม? "+predictResult

today = [15, 44]
R = knn(today)
print(R)