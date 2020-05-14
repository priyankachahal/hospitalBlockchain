import pandas as pd
import pickle
import keras

dataset = pd.read_csv("/home/deeksha/Documents/test/003_1.csv")
# meta_dataset = pd.read_csv()

dataset = dataset['ECG']
dataset = dataset.iloc[1000:]
dataset = dataset[:-1000]

model = pickle.load(open('/home/deeksha/Documents/test/ecg_model.pkl','rb'))
print(model.predict(dataset))