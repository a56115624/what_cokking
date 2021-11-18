import pandas as pd
from urllib.request import urlretrieve
url = "https://github.com/Elwing-Chou/tibaml1027/raw/main/train.csv"
urlretrieve(url, "train.csv")
train = pd.read_csv("train.csv", encoding="utf-8")
url = "https://github.com/Elwing-Chou/tibaml1027/raw/main/test.csv"
urlretrieve(url, "test.csv")
test = pd.read_csv("test.csv", encoding="utf-8")
#test


# concat
datas = pd.concat([train, test], axis=0, ignore_index=True)
datas = datas.drop(["PassengerId", "Survived"], axis=1)
datas